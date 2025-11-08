from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, BusRoute, BusStop, RouteRegistration, Notification, QuickQuery
from datetime import date, timedelta

class StudentSignUpForm(UserCreationForm):
    """Student signup form."""
    
    usn = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'USN (e.g., 1CR21CS001)'
        })
    )
    
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        })
    )
    
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number'
        })
    )
    
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input'
        })
    )
    
    class Meta:
        model = User
        fields = ('usn', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm Password'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['usn']
        user.role = 'student'
        if commit:
            user.save()
        return user


class DriverSignUpForm(UserCreationForm):
    """Driver signup form."""
    
    emp_no = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Employee Number (e.g., EMP001)'
        })
    )
    
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        })
    )
    
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number'
        })
    )
    
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input'
        })
    )
    
    class Meta:
        model = User
        fields = ('emp_no', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(DriverSignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm Password'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['emp_no']
        user.role = 'driver'
        if commit:
            user.save()
        return user


class AdminSignUpForm(UserCreationForm):
    """Admin signup form."""
    
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Username'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm Password'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'admin'
        user.is_staff = True
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """Custom login form."""
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'USN / Employee No / Username'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Password'
        })
    )


class RouteRegistrationForm(forms.ModelForm):
    """Form for students to register for a bus route."""
    
    route = forms.ModelChoiceField(
        queryset=BusRoute.objects.filter(status='active'),
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'route-select'
        }),
        empty_label="Select a route"
    )
    
    bus_stop = forms.ModelChoiceField(
        queryset=BusStop.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'stop-select'
        }),
        empty_label="Select your boarding stop"
    )
    
    start_date = forms.DateField(
        initial=date.today(),
        widget=forms.DateInput(attrs={
            'class': 'form-input',
            'type': 'date'
        })
    )
    
    special_requirements = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': 'Any special requirements or notes (optional)',
            'rows': 3
        })
    )
    
    class Meta:
        model = RouteRegistration
        fields = ['route', 'bus_stop', 'start_date', 'special_requirements']
    
    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)
        
        # If route is selected, filter bus stops
        if 'route' in self.data:
            try:
                route_id = int(self.data.get('route'))
                self.fields['bus_stop'].queryset = BusStop.objects.filter(route_id=route_id).exclude(
                    stop_name='SJB Institute of Technology'
                ).order_by('stop_order')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['bus_stop'].queryset = self.instance.route.stops.exclude(
                stop_name='SJB Institute of Technology'
            ).order_by('stop_order')
    
    def clean(self):
        cleaned_data = super().clean()
        route = cleaned_data.get('route')
        bus_stop = cleaned_data.get('bus_stop')
        
        # Check if student already has an active registration
        if self.student:
            existing = RouteRegistration.objects.filter(
                student=self.student,
                status='active'
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing.exists():
                raise forms.ValidationError(
                    'You already have an active route registration. Please cancel it before registering for a new route.'
                )
        
        # Validate bus stop belongs to selected route
        if route and bus_stop:
            if bus_stop.route != route:
                raise forms.ValidationError('Selected stop does not belong to the selected route.')
        
        # Check available seats
        if route:
            if route.get_available_seats() <= 0:
                raise forms.ValidationError('Sorry, this route is full. No seats available.')
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.student:
            instance.student = self.student
        if not instance.monthly_fee:
            instance.monthly_fee = instance.bus_stop.base_fare
        if commit:
            instance.save()
        return instance


class ProfileEditForm(forms.ModelForm):
    """Form for editing user profile."""
    
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        })
    )
    
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number'
        })
    )
    
    gender = forms.ChoiceField(
        required=False,
        choices=[('', 'Select Gender')] + list(User.GENDER_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-input'
        })
    )
    
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-input',
            'accept': 'image/*'
        })
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'profile_image']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email is already taken by another user
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email


class PasswordChangeForm(forms.Form):
    """Form for changing user password."""
    
    current_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter current password'
        }),
        label='Current Password'
    )
    
    new_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter new password'
        }),
        label='New Password',
        min_length=8,
        help_text='Password must be at least 8 characters long.'
    )
    
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm new password'
        }),
        label='Confirm New Password'
    )
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    
    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise forms.ValidationError('Current password is incorrect.')
        return current_password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError('New passwords do not match.')
        
        return cleaned_data
    
    def save(self):
        """Save the new password."""
        new_password = self.cleaned_data.get('new_password')
        self.user.set_password(new_password)
        self.user.save()
        return self.user


class NotificationForm(forms.ModelForm):
    """Form for creating notifications."""
    
    class Meta:
        model = Notification
        fields = ['title', 'message', 'message_type', 'route', 
                 'visible_to_students', 'visible_to_drivers', 'visible_to_admins']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Notification Title'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your message here...',
                'rows': 4
            }),
            'message_type': forms.Select(attrs={'class': 'form-input'}),
            'route': forms.Select(attrs={'class': 'form-input'}),
        }
        help_texts = {
            'route': 'Select a specific route or leave blank for system-wide notification',
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Store user for later use
        self.user = user
        
        # Make route optional with a blank choice
        self.fields['route'].required = False
        self.fields['route'].empty_label = "All Routes (System-wide)"
        
        # Filter routes and visibility based on user role
        if user:
            if user.role == 'driver':
                # Driver can only send notifications for their assigned route
                try:
                    self.fields['route'].queryset = BusRoute.objects.filter(driver=user)
                    self.fields['route'].required = True
                    self.fields['route'].empty_label = None
                except:
                    self.fields['route'].queryset = BusRoute.objects.none()
                
                # Hide visibility checkboxes for drivers - auto-set in save()
                self.fields['visible_to_students'].widget = forms.HiddenInput()
                self.fields['visible_to_drivers'].widget = forms.HiddenInput()
                self.fields['visible_to_admins'].widget = forms.HiddenInput()
                
            elif user.role == 'admin':
                # Admin can send to any route
                self.fields['route'].queryset = BusRoute.objects.filter(status='active')
                # Admin keeps visibility checkboxes visible
    
    def save(self, commit=True):
        notification = super().save(commit=False)
        
        # Apply strict visibility rules based on user role
        if self.user:
            if self.user.role == 'driver':
                # Driver: visible to students of their route and admins only
                notification.visible_to_students = True
                notification.visible_to_drivers = False
                notification.visible_to_admins = True
            elif self.user.role == 'student':
                # Student: visible to driver of their route and admins only
                notification.visible_to_students = False
                notification.visible_to_drivers = True
                notification.visible_to_admins = True
            # Admin keeps the form values (no override)
        
        if commit:
            notification.save()
        return notification


class QuickQueryForm(forms.ModelForm):
    """Form for student quick queries."""
    
    class Meta:
        model = QuickQuery
        fields = ['query_type', 'additional_message']
        widgets = {
            'query_type': forms.Select(attrs={'class': 'form-input'}),
            'additional_message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Add any additional details (optional)',
                'rows': 3
            }),
        }


class QueryResponseForm(forms.ModelForm):
    """Form for responding to student queries."""
    
    class Meta:
        model = QuickQuery
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Type your response here...',
                'rows': 3
            }),
        }
