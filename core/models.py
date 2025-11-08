from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from decimal import Decimal

class User(AbstractUser):
    """Custom user model with role-based access."""
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('student', 'Student'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    # Student fields
    usn = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='USN')
    
    # Driver fields
    emp_no = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Employee Number')
    
    # Common fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Fix for Django's default User model conflict
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
    def __str__(self):
        if self.role == 'student' and self.usn:
            return f"{self.usn} - {self.get_full_name()} ({self.get_role_display()})"
        elif self.role == 'driver' and self.emp_no:
            return f"{self.emp_no} - {self.get_full_name()} ({self.get_role_display()})"
        return f"{self.username} ({self.get_role_display()})"
    
    class Meta:
        ordering = ['-created_at']


class BusRoute(models.Model):
    """Bus route model representing different routes in Bangalore."""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    name = models.CharField(max_length=100, help_text="Route name (e.g., Route 1 - North Bangalore)")
    route_number = models.CharField(max_length=10, unique=True, help_text="Unique route identifier")
    description = models.TextField(blank=True)
    bus_number = models.CharField(max_length=20, help_text="Bus registration number")
    capacity = models.IntegerField(default=40, validators=[MinValueValidator(1)])
    driver = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, 
                                  related_name='assigned_route', limit_choices_to={'role': 'driver'})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    departure_time = models.TimeField(help_text="Departure time from SJB Institute")
    arrival_time = models.TimeField(help_text="Expected arrival time at SJB Institute")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.route_number} - {self.name}"
    
    def get_total_stops(self):
        return self.stops.count()
    
    def get_registered_students_count(self):
        return self.registrations.filter(status='active').count()
    
    def get_available_seats(self):
        return self.capacity - self.get_registered_students_count()
    
    class Meta:
        ordering = ['route_number']


class BusStop(models.Model):
    """Individual bus stop in a route."""
    
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='stops')
    stop_name = models.CharField(max_length=200)
    stop_order = models.IntegerField(help_text="Order of stop in the route (1 being first)")
    distance_from_sjb = models.DecimalField(max_digits=5, decimal_places=2, 
                                            help_text="Distance in kilometers from SJB Institute")
    pickup_time = models.TimeField(help_text="Expected pickup time at this stop")
    base_fare = models.DecimalField(max_digits=6, decimal_places=2, 
                                    validators=[MinValueValidator(Decimal('0.01'))],
                                    help_text="Monthly fare for this stop")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def __str__(self):
        return f"{self.route.route_number} - Stop {self.stop_order}: {self.stop_name}"
    
    class Meta:
        ordering = ['route', 'stop_order']
        unique_together = ['route', 'stop_order']


class RouteRegistration(models.Model):
    """Student registration for a specific bus route and stop."""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending Approval'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial Payment'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='route_registrations',
                               limit_choices_to={'role': 'student'})
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='registrations')
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    monthly_fee = models.DecimalField(max_digits=6, decimal_places=2)
    registration_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    special_requirements = models.TextField(blank=True, help_text="Any special requirements or notes")
    
    def __str__(self):
        return f"{self.student.usn} - {self.route.route_number} - {self.bus_stop.stop_name}"
    
    def save(self, *args, **kwargs):
        # Set monthly fee from bus stop if not already set
        if not self.monthly_fee:
            self.monthly_fee = self.bus_stop.base_fare
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-registration_date']
        # Note: One active/pending registration per student is enforced in views, not at DB level
        # This allows students to re-register for routes they previously cancelled


class Attendance(models.Model):
    """Track daily attendance for students on the bus."""
    
    registration = models.ForeignKey(RouteRegistration, on_delete=models.CASCADE, 
                                    related_name='attendance_records')
    date = models.DateField()
    boarded = models.BooleanField(default=False)
    boarding_time = models.TimeField(null=True, blank=True)
    marked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
                                  related_name='marked_attendance')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        status = "Present" if self.boarded else "Absent"
        return f"{self.registration.student.usn} - {self.date} - {status}"
    
    class Meta:
        ordering = ['-date']
        unique_together = ['registration', 'date']


class Notification(models.Model):
    """System notifications and messages."""
    
    MESSAGE_TYPE_CHOICES = [
        ('delay', 'Bus Delay'),
        ('arrival', 'Bus Arrival'),
        ('route_change', 'Route Change'),
        ('maintenance', 'Maintenance'),
        ('emergency', 'Emergency'),
        ('general', 'General Announcement'),
        ('query', 'Student Query'),
    ]
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES, default='general')
    
    # Sender information
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    
    # Route-specific notifications (optional - if None, visible to all)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='notifications', help_text="Leave blank for system-wide notification")
    
    # Visibility controls
    visible_to_students = models.BooleanField(default=True)
    visible_to_drivers = models.BooleanField(default=True)
    visible_to_admins = models.BooleanField(default=True)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_resolved = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='resolved_notifications')
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        route_info = f" - {self.route.route_number}" if self.route else " - System Wide"
        return f"{self.get_message_type_display()}{route_info} by {self.sender.get_full_name()}"
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['route', 'is_active']),
        ]


class QuickQuery(models.Model):
    """Pre-defined quick queries for students."""
    
    QUERY_TYPE_CHOICES = [
        ('bus_late', 'Is the bus running late?'),
        ('bus_location', 'Where is the bus now?'),
        ('route_change', 'Any route changes today?'),
        ('driver_contact', 'How to contact driver?'),
        ('fare_query', 'Question about fare'),
        ('schedule_query', 'Question about schedule'),
        ('other', 'Other'),
    ]
    
    query_type = models.CharField(max_length=20, choices=QUERY_TYPE_CHOICES)
    student = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='queries',
                               limit_choices_to={'role': 'student'})
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='queries')
    bus_stop = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='queries',
                                 help_text="Student's bus stop for this query")
    additional_message = models.TextField(blank=True, help_text="Optional additional details")
    
    # Response
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True)
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='answered_queries')
    answered_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_query_type_display()} - {self.student.usn}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Quick Queries"


class BusLocation(models.Model):
    """Model to store real-time bus location data from GPS."""
    
    driver = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='bus_locations',
                              limit_choices_to={'role': 'driver'})
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, 
                             related_name='bus_locations')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                               help_text="Speed in km/h")
    heading = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                 help_text="Direction in degrees (0-360)")
    accuracy = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True,
                                  help_text="GPS accuracy in meters")
    is_active = models.BooleanField(default=True,
                                   help_text="Whether the driver is currently sharing location")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.driver.get_full_name()} - {self.route.route_name} ({self.timestamp})"
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Bus Location"
        verbose_name_plural = "Bus Locations"
        indexes = [
            models.Index(fields=['driver', '-timestamp']),
            models.Index(fields=['route', '-timestamp']),
            models.Index(fields=['is_active', '-timestamp']),
        ]
