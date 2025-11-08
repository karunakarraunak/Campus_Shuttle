from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
from django.views.decorators.http import require_http_methods
import json
from .forms import (StudentSignUpForm, DriverSignUpForm, AdminSignUpForm, LoginForm, 
                   RouteRegistrationForm, ProfileEditForm, PasswordChangeForm,
                   NotificationForm, QuickQueryForm, QueryResponseForm)
from .models import BusRoute, BusStop, RouteRegistration, Notification, QuickQuery, BusLocation
from datetime import date, timedelta

def landing_page(request):
    """Render the landing page."""
    return render(request, 'core/landing.html')


def signup_view(request):
    """Handle user registration with role selection."""
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    role = request.GET.get('role', request.POST.get('role', ''))
    
    if request.method == 'POST':
        if role == 'student':
            form = StudentSignUpForm(request.POST)
        elif role == 'driver':
            form = DriverSignUpForm(request.POST)
        elif role == 'admin':
            form = AdminSignUpForm(request.POST)
        else:
            messages.error(request, 'Please select a valid role.')
            return redirect('core:signup')
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome! Your account has been created.')
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        if role == 'student':
            form = StudentSignUpForm()
        elif role == 'driver':
            form = DriverSignUpForm()
        elif role == 'admin':
            form = AdminSignUpForm()
        else:
            form = None
    
    return render(request, 'core/signup.html', {'form': form, 'role': role})


def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back!')
                return redirect('core:dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('core:landing')


@login_required
def dashboard_view(request):
    """Render role-based dashboard."""
    user = request.user
    context = {
        'user': user,
        'role': user.role,
    }
    
    # Add role-specific context
    if user.role == 'student':
        # Get student's active or pending registration (get latest if multiple exist)
        try:
            registration = RouteRegistration.objects.filter(
                student=user, 
                status__in=['active', 'pending']
            ).order_by('-registration_date').first()
            context['registration'] = registration
            
            # Get recent notifications for student
            if registration:
                context['recent_notifications'] = Notification.objects.filter(
                    is_active=True,
                    visible_to_students=True
                ).filter(
                    Q(route=registration.route) | Q(route__isnull=True)
                ).order_by('-created_at')[:3]
            else:
                context['recent_notifications'] = Notification.objects.filter(
                    is_active=True,
                    visible_to_students=True,
                    route__isnull=True
                ).order_by('-created_at')[:3]
            
            # Get unanswered queries count
            context['unanswered_queries'] = QuickQuery.objects.filter(
                student=user,
                is_answered=False
            ).count()
            
        except RouteRegistration.DoesNotExist:
            context['registration'] = None
            context['recent_notifications'] = Notification.objects.filter(
                is_active=True,
                visible_to_students=True,
                route__isnull=True
            ).order_by('-created_at')[:3]
            
    elif user.role == 'driver':
        # Get driver's assigned route (OneToOne relationship)
        try:
            context['assigned_route'] = user.assigned_route
            # Get recent notifications for driver
            context['recent_notifications'] = Notification.objects.filter(
                is_active=True,
                visible_to_drivers=True
            ).filter(
                Q(route=user.assigned_route) | Q(route__isnull=True)
            ).order_by('-created_at')[:5]
            
            # Get unresolved queries count
            context['unresolved_queries_count'] = QuickQuery.objects.filter(
                route=user.assigned_route,
                is_answered=False
            ).count()
            
            # Get recently answered queries
            context['answered_queries'] = QuickQuery.objects.filter(
                route=user.assigned_route,
                is_answered=True
            ).order_by('-answered_at')[:10]
        except:
            context['assigned_route'] = None
            context['recent_notifications'] = Notification.objects.filter(
                is_active=True,
                visible_to_drivers=True,
                route__isnull=True
            ).order_by('-created_at')[:5]
            context['unresolved_queries_count'] = 0
            context['answered_queries'] = QuickQuery.objects.none()
            
    elif user.role == 'admin':
        # Get statistics
        context['total_routes'] = BusRoute.objects.count()
        context['total_students'] = RouteRegistration.objects.filter(status='active').count()
        context['total_drivers'] = user.__class__.objects.filter(role='driver').count()
        context['pending_registrations'] = RouteRegistration.objects.filter(status='pending').count()
        
        # Get recent notifications
        context['recent_notifications'] = Notification.objects.filter(
            is_active=True
        ).order_by('-created_at')[:5]
        
        # Get all unresolved queries
        context['unresolved_queries_count'] = QuickQuery.objects.filter(
            is_answered=False
        ).count()
    
    # Render different templates based on role
    if user.role == 'admin':
        return render(request, 'core/dashboard_admin.html', context)
    elif user.role == 'driver':
        return render(request, 'core/dashboard_driver.html', context)
    else:  # student
        return render(request, 'core/dashboard_student.html', context)


@login_required
def routes_list(request):
    """Display all available routes."""
    routes = BusRoute.objects.filter(status='active').prefetch_related('stops')
    
    # Check if student already has active or pending registration
    user_registration = None
    if request.user.role == 'student':
        user_registration = RouteRegistration.objects.filter(
            student=request.user,
            status__in=['active', 'pending']
        ).order_by('-registration_date').first()
        
        if user_registration:
            if user_registration.status == 'active':
                messages.info(request, f'You are already registered for {user_registration.route.route_number}. Cancel your current registration if you want to switch routes.')
            else:  # pending
                messages.info(request, f'You have a pending registration for {user_registration.route.route_number}. Wait for approval or cancel it to register for another route.')
    
    context = {
        'routes': routes,
        'user': request.user,
        'user_registration': user_registration,
    }
    return render(request, 'core/routes_list.html', context)


@login_required
def route_detail(request, route_id):
    """Display details of a specific route."""
    route = get_object_or_404(BusRoute, id=route_id)
    stops = route.stops.all().order_by('stop_order')
    
    # Check if user has registration for this route
    user_registration = None
    if request.user.role == 'student':
        try:
            user_registration = RouteRegistration.objects.get(
                student=request.user,
                route=route,
                status='active'
            )
        except RouteRegistration.DoesNotExist:
            pass
    
    context = {
        'route': route,
        'stops': stops,
        'user_registration': user_registration,
        'available_seats': route.get_available_seats(),
    }
    return render(request, 'core/route_detail.html', context)


@login_required
def register_route(request):
    """Handle route registration for students."""
    if request.user.role != 'student':
        messages.error(request, 'Only students can register for routes.')
        return redirect('core:dashboard')
    
    # Check if student already has active or pending registration (enforce one route per student)
    existing = RouteRegistration.objects.filter(
        student=request.user,
        status__in=['active', 'pending']
    ).order_by('-registration_date').first()
    
    if existing:
        if existing.status == 'active':
            messages.warning(request, f'You are already registered for {existing.route.route_number}. Cancel your current registration before registering for a new route.')
        else:  # pending
            messages.warning(request, f'You have a pending registration for {existing.route.route_number}. Please wait for admin approval or cancel it before registering for another route.')
        return redirect('core:my_registration')
    
    if request.method == 'POST':
        form = RouteRegistrationForm(request.POST, student=request.user)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = request.user
            registration.status = 'pending'
            registration.save()
            messages.success(request, 
                f'Route registration submitted successfully! Waiting for admin approval. Monthly fee: ₹{registration.monthly_fee}')
            return redirect('core:my_registration')
    else:
        form = RouteRegistrationForm(student=request.user)
    
    context = {
        'form': form,
        'routes': BusRoute.objects.filter(status='active'),
    }
    return render(request, 'core/register_route.html', context)


@login_required
def my_registration(request):
    """Display student's route registration."""
    if request.user.role != 'student':
        messages.error(request, 'Access denied.')
        return redirect('core:dashboard')
    
    # Get the latest active or pending registration
    registration = RouteRegistration.objects.filter(
        student=request.user,
        status__in=['active', 'pending']
    ).order_by('-registration_date').first()
    
    context = {
        'registration': registration,
    }
    return render(request, 'core/my_registration.html', context)


@login_required
def cancel_registration(request, registration_id):
    """Cancel a route registration."""
    registration = get_object_or_404(RouteRegistration, id=registration_id)
    
    # Check permission
    if request.user.role == 'student' and registration.student != request.user:
        messages.error(request, 'You can only cancel your own registration.')
        return redirect('core:dashboard')
    
    # Cancel the registration directly
    registration.status = 'cancelled'
    registration.save()
    messages.success(request, 'Route registration cancelled successfully.')
    return redirect('core:dashboard')


def get_route_stops(request, route_id):
    """AJAX endpoint to get stops for a route."""
    stops = BusStop.objects.filter(route_id=route_id).exclude(
        stop_name='SJB Institute of Technology'
    ).order_by('stop_order')
    
    stops_data = [{
        'id': stop.id,
        'name': stop.stop_name,
        'time': stop.pickup_time.strftime('%H:%M'),
        'fare': float(stop.base_fare),
        'distance': float(stop.distance_from_sjb)
    } for stop in stops]
    
    return JsonResponse({'stops': stops_data})


@login_required
def edit_profile(request):
    """Edit user profile with profile picture upload and password change."""
    profile_form = ProfileEditForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)
    
    if request.method == 'POST':
        # Check which form was submitted
        if 'update_profile' in request.POST:
            profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('core:edit_profile')
            else:
                messages.error(request, 'Please correct the errors in the profile form.')
        
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                # Update session to prevent logout after password change
                from django.contrib.auth import update_session_auth_hash
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password changed successfully!')
                return redirect('core:edit_profile')
            else:
                messages.error(request, 'Please correct the errors in the password form.')
    
    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'core/edit_profile.html', context)


# ==================== NOTIFICATION VIEWS ====================

@login_required
def notifications_list(request):
    """Display all notifications relevant to the user."""
    user = request.user
    
    # Filter notifications based on user role
    if user.role == 'student':
        # Get student's route
        registration = RouteRegistration.objects.filter(
            student=user,
            status__in=['active', 'pending']
        ).order_by('-registration_date').first()
        
        if registration:
            # Show route-specific and system-wide notifications
            notifications = Notification.objects.filter(
                is_active=True,
                visible_to_students=True
            ).filter(
                Q(route=registration.route) | Q(route__isnull=True)
            )
        else:
            # Show only system-wide notifications
            notifications = Notification.objects.filter(
                is_active=True,
                visible_to_students=True,
                route__isnull=True
            )
    
    elif user.role == 'driver':
        # Show notifications for driver's assigned route and system-wide
        try:
            assigned_route = user.assigned_route
            notifications = Notification.objects.filter(
                is_active=True,
                visible_to_drivers=True
            ).filter(
                Q(route=assigned_route) | Q(route__isnull=True)
            )
        except:
            notifications = Notification.objects.filter(
                is_active=True,
                visible_to_drivers=True,
                route__isnull=True
            )
    
    elif user.role == 'admin':
        # Admins see all notifications
        notifications = Notification.objects.filter(is_active=True)
    
    else:
        notifications = Notification.objects.none()
    
    # Get unresolved queries for admins and drivers
    unresolved_queries = None
    if user.role == 'admin':
        unresolved_queries = QuickQuery.objects.filter(is_answered=False)
    elif user.role == 'driver':
        try:
            unresolved_queries = QuickQuery.objects.filter(
                route=user.assigned_route,
                is_answered=False
            )
        except:
            pass
    
    context = {
        'notifications': notifications,
        'unresolved_queries': unresolved_queries,
    }
    return render(request, 'core/notifications.html', context)


@login_required
def create_notification(request):
    """Create a new notification (Driver/Admin only)."""
    if request.user.role not in ['driver', 'admin']:
        messages.error(request, 'You do not have permission to create notifications.')
        return redirect('core:notifications_list')
    
    if request.method == 'POST':
        form = NotificationForm(request.POST, user=request.user)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.sender = request.user
            notification.save()
            messages.success(request, 'Notification posted successfully!')
            return redirect('core:notifications_list')
    else:
        form = NotificationForm(user=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'core/create_notification.html', context)


@login_required
def student_queries(request):
    """View for students to submit quick queries."""
    if request.user.role != 'student':
        messages.error(request, 'Access denied.')
        return redirect('core:dashboard')
    
    # Get student's route
    registration = RouteRegistration.objects.filter(
        student=request.user,
        status__in=['active', 'pending']
    ).order_by('-registration_date').first()
    
    if not registration:
        messages.warning(request, 'You need to register for a route first.')
        return redirect('core:register_route')
    
    if request.method == 'POST':
        form = QuickQueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.student = request.user
            query.route = registration.route
            query.bus_stop = registration.bus_stop  # Automatically add student's bus stop
            query.save()
            messages.success(request, 'Your query has been submitted! You will be notified once answered.')
            return redirect('core:student_queries')
    else:
        form = QuickQueryForm()
    
    # Get student's previous queries
    my_queries = QuickQuery.objects.filter(student=request.user)
    
    context = {
        'form': form,
        'my_queries': my_queries,
        'registration': registration,
    }
    return render(request, 'core/student_queries.html', context)


@login_required
def answer_query(request, query_id):
    """Answer a student query (Driver/Admin only)."""
    if request.user.role not in ['driver', 'admin']:
        messages.error(request, 'Access denied.')
        return redirect('core:dashboard')
    
    query = get_object_or_404(QuickQuery, id=query_id)
    
    # Drivers can only answer queries for their route
    if request.user.role == 'driver':
        try:
            if query.route != request.user.assigned_route:
                messages.error(request, 'You can only answer queries for your assigned route.')
                return redirect('core:notifications_list')
        except:
            messages.error(request, 'You are not assigned to any route.')
            return redirect('core:dashboard')
    
    if request.method == 'POST':
        form = QueryResponseForm(request.POST, instance=query)
        if form.is_valid():
            query = form.save(commit=False)
            query.is_answered = True
            query.answered_by = request.user
            query.answered_at = timezone.now()
            query.save()
            messages.success(request, 'Response submitted successfully!')
            return redirect('core:notifications_list')
    else:
        form = QueryResponseForm(instance=query)
    
    context = {
        'form': form,
        'query': query,
    }
    return render(request, 'core/answer_query.html', context)


@login_required
def resolve_notification(request, notification_id):
    """Mark a notification as resolved (Admin/Sender only)."""
    notification = get_object_or_404(Notification, id=notification_id)
    
    # Only admin or the sender can resolve
    if request.user.role != 'admin' and notification.sender != request.user:
        messages.error(request, 'You do not have permission to resolve this notification.')
        return redirect('core:notifications_list')
    
    notification.is_resolved = True
    notification.resolved_by = request.user
    notification.resolved_at = timezone.now()
    notification.save()
    
    messages.success(request, 'Notification marked as resolved.')
    return redirect('core:notifications_list')


@login_required
def track_bus(request):
    """
    Display real-time bus tracking with OpenStreetMap.
    - Students: Can view only their registered route's driver location
    - Admin: Can view all driver locations
    - Drivers: Can share their location but cannot view others
    """
    context = {
        'user_role': request.user.role,
    }
    
    # If student, get their registered route
    if request.user.role == 'student':
        registration = RouteRegistration.objects.filter(
            student=request.user,
            status='approved'
        ).select_related('route').first()
        
        if registration:
            context['registered_route'] = registration.route
        else:
            context['no_registration'] = True
    
    return render(request, 'core/track_bus.html', context)


@login_required
@require_http_methods(["POST"])
def update_location(request):
    """
    API endpoint for drivers to update their GPS location.
    """
    if request.user.role != 'driver':
        return JsonResponse({'error': 'Only drivers can update location'}, status=403)
    
    try:
        data = json.loads(request.body)
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        speed = data.get('speed')
        heading = data.get('heading')
        accuracy = data.get('accuracy')
        is_active = data.get('is_active', True)
        route_id = data.get('route_id')
        
        if latitude is None or longitude is None:
            return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)
        
        try:
            lat = float(latitude)
            lng = float(longitude)
            
            if not (-90 <= lat <= 90):
                return JsonResponse({'error': 'Invalid latitude value'}, status=400)
            if not (-180 <= lng <= 180):
                return JsonResponse({'error': 'Invalid longitude value'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid coordinate values'}, status=400)
        
        # Get driver's assigned route
        if route_id:
            driver_route = get_object_or_404(BusRoute, id=route_id, driver=request.user)
        else:
            driver_route = BusRoute.objects.filter(driver=request.user).first()
            if not driver_route:
                return JsonResponse({'error': 'No route assigned to driver'}, status=400)
        
        # Create location record
        location = BusLocation.objects.create(
            driver=request.user,
            route=driver_route,
            latitude=lat,
            longitude=lng,
            speed=speed,
            heading=heading,
            accuracy=accuracy,
            is_active=is_active
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Location updated successfully',
            'timestamp': location.timestamp.isoformat()
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def get_locations(request):
    """
    API endpoint to get current bus locations based on user role.
    - Students: Returns only their registered route's driver location
    - Admin: Returns all active driver locations
    - Drivers: Returns their own location
    """
    time_threshold = timezone.now() - timedelta(minutes=5)
    
    if request.user.role == 'admin':
        # Admin can see all active locations
        locations = BusLocation.objects.filter(
            is_active=True,
            updated_at__gte=time_threshold
        ).select_related('driver', 'route').order_by('driver', '-timestamp').distinct('driver')
        
    elif request.user.role == 'student':
        # Student can only see their registered route's driver
        registration = RouteRegistration.objects.filter(
            student=request.user,
            status='approved'
        ).select_related('route').first()
        
        if not registration:
            return JsonResponse({'locations': []})
        
        locations = BusLocation.objects.filter(
            route=registration.route,
            is_active=True,
            updated_at__gte=time_threshold
        ).select_related('driver', 'route').order_by('driver', '-timestamp').distinct('driver')
    
    elif request.user.role == 'driver':
        # Driver can only see their own location
        locations = BusLocation.objects.filter(
            driver=request.user,
            is_active=True,
            updated_at__gte=time_threshold
        ).select_related('driver', 'route').order_by('-timestamp')[:1]
    
    else:
        return JsonResponse({'locations': []})
    
    # Format response
    locations_data = []
    for location in locations:
        locations_data.append({
            'driver_id': location.driver.id,
            'driver_name': location.driver.get_full_name(),
            'driver_phone': location.driver.phone_number,
            'route_id': location.route.id,
            'route_name': location.route.route_name,
            'route_number': location.route.route_number,
            'latitude': float(location.latitude),
            'longitude': float(location.longitude),
            'speed': float(location.speed) if location.speed else None,
            'heading': float(location.heading) if location.heading else None,
            'accuracy': float(location.accuracy) if location.accuracy else None,
            'timestamp': location.timestamp.isoformat(),
            'updated_at': location.updated_at.isoformat(),
            'minutes_ago': int((timezone.now() - location.updated_at).total_seconds() / 60)
        })
    
    return JsonResponse({'locations': locations_data})
    return redirect('core:notifications_list')
