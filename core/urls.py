from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Profile management
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    # Route management
    path('routes/', views.routes_list, name='routes_list'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('routes/register/', views.register_route, name='register_route'),
    path('routes/my-registration/', views.my_registration, name='my_registration'),
    path('routes/cancel/<int:registration_id>/', views.cancel_registration, name='cancel_registration'),
    
    # AJAX endpoints
    path('api/route-stops/<int:route_id>/', views.get_route_stops, name='get_route_stops'),
    
    # Notifications
    path('notifications/', views.notifications_list, name='notifications_list'),
    path('notifications/create/', views.create_notification, name='create_notification'),
    path('notifications/resolve/<int:notification_id>/', views.resolve_notification, name='resolve_notification'),
    
    # Student Queries
    path('queries/', views.student_queries, name='student_queries'),
    path('queries/answer/<int:query_id>/', views.answer_query, name='answer_query'),
    
    # GPS Bus Tracking
    path('track-bus/', views.track_bus, name='track_bus'),
    path('api/update-location/', views.update_location, name='update_location'),
    path('api/get-locations/', views.get_locations, name='get_locations'),
]
