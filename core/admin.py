from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, BusRoute, BusStop, RouteRegistration, Attendance, Notification, QuickQuery, BusLocation

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User Admin."""
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'usn', 'emp_no')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'usn', 'emp_no', 'phone_number', 'gender', 'profile_image')}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'usn', 'emp_no', 'phone_number', 'gender', 'email', 'first_name', 'last_name')}),
    )


class BusStopInline(admin.TabularInline):
    """Inline admin for bus stops."""
    model = BusStop
    extra = 1
    ordering = ['stop_order']


@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    """Admin for bus routes."""
    list_display = ('route_number', 'name', 'bus_number', 'driver', 'status', 'departure_time', 
                   'get_total_stops', 'get_registered_students_count', 'capacity')
    list_filter = ('status', 'driver')
    search_fields = ('route_number', 'name', 'bus_number')
    inlines = [BusStopInline]
    list_editable = ('status',)
    
    fieldsets = (
        ('Route Information', {
            'fields': ('route_number', 'name', 'description', 'bus_number', 'capacity')
        }),
        ('Assignment', {
            'fields': ('driver', 'status')
        }),
        ('Schedule', {
            'fields': ('departure_time', 'arrival_time')
        }),
    )


@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    """Admin for bus stops."""
    list_display = ('route', 'stop_order', 'stop_name', 'distance_from_sjb', 'pickup_time', 'base_fare')
    list_filter = ('route',)
    search_fields = ('stop_name',)
    ordering = ('route', 'stop_order')


@admin.register(RouteRegistration)
class RouteRegistrationAdmin(admin.ModelAdmin):
    """Admin for route registrations."""
    list_display = ('student', 'route', 'bus_stop', 'status', 'payment_status', 
                   'monthly_fee', 'registration_date', 'start_date')
    list_filter = ('status', 'payment_status', 'route')
    search_fields = ('student__usn', 'student__first_name', 'student__last_name')
    date_hierarchy = 'registration_date'
    list_editable = ('status', 'payment_status')
    actions = ['approve_registrations', 'reject_registrations']
    
    fieldsets = (
        ('Student & Route', {
            'fields': ('student', 'route', 'bus_stop')
        }),
        ('Status', {
            'fields': ('status', 'payment_status', 'monthly_fee')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Additional Info', {
            'fields': ('special_requirements',)
        }),
    )
    
    @admin.action(description='Approve selected registrations')
    def approve_registrations(self, request, queryset):
        """Approve pending registrations."""
        updated = queryset.filter(status='pending').update(status='active')
        self.message_user(request, f'{updated} registration(s) approved successfully.')
    
    @admin.action(description='Reject selected registrations')
    def reject_registrations(self, request, queryset):
        """Reject pending registrations."""
        updated = queryset.filter(status='pending').update(status='cancelled')
        self.message_user(request, f'{updated} registration(s) rejected.')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """Admin for attendance records."""
    list_display = ('registration', 'date', 'boarded', 'boarding_time', 'marked_by')
    list_filter = ('boarded', 'date', 'registration__route')
    search_fields = ('registration__student__usn', 'registration__student__first_name')
    date_hierarchy = 'date'
    list_editable = ('boarded',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin for notifications."""
    list_display = ('title', 'message_type', 'sender', 'route', 
                   'is_active', 'is_resolved', 'created_at')
    list_filter = ('message_type', 'is_active', 'is_resolved', 'route')
    search_fields = ('title', 'message', 'sender__username')
    date_hierarchy = 'created_at'
    list_editable = ('is_active', 'is_resolved')
    readonly_fields = ('created_at', 'updated_at', 'resolved_at')
    
    fieldsets = (
        ('Message Details', {
            'fields': ('title', 'message', 'message_type')
        }),
        ('Sender & Target', {
            'fields': ('sender', 'route')
        }),
        ('Visibility', {
            'fields': ('visible_to_students', 'visible_to_drivers', 'visible_to_admins')
        }),
        ('Status', {
            'fields': ('is_active', 'is_resolved', 'resolved_by', 'resolved_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(QuickQuery)
class QuickQueryAdmin(admin.ModelAdmin):
    """Admin for quick queries."""
    list_display = ('query_type', 'student', 'route', 'is_answered', 'created_at')
    list_filter = ('query_type', 'is_answered', 'route')
    search_fields = ('student__usn', 'student__first_name', 'additional_message')
    date_hierarchy = 'created_at'
    list_editable = ('is_answered',)
    readonly_fields = ('created_at', 'answered_at')
    
    fieldsets = (
        ('Query Details', {
            'fields': ('query_type', 'student', 'route', 'additional_message')
        }),
        ('Response', {
            'fields': ('is_answered', 'answer', 'answered_by', 'answered_at')
        }),
        ('Timestamp', {
            'fields': ('created_at',)
        }),
    )


@admin.register(BusLocation)
class BusLocationAdmin(admin.ModelAdmin):
    """Admin for bus GPS location tracking."""
    list_display = ('driver', 'route', 'latitude', 'longitude', 'speed', 'is_active', 'timestamp', 'updated_at')
    list_filter = ('is_active', 'route', 'driver')
    search_fields = ('driver__first_name', 'driver__last_name', 'driver__emp_no', 'route__route_number', 'route__route_name')
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp', 'updated_at')
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Location Details', {
            'fields': ('driver', 'route', 'latitude', 'longitude')
        }),
        ('GPS Data', {
            'fields': ('speed', 'heading', 'accuracy')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('timestamp', 'updated_at')
        }),
    )
    
    def get_queryset(self, request):
        """Optimize query with select_related."""
        return super().getqueryset(request).select_related('driver', 'route')
