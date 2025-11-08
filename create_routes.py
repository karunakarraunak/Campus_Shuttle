import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_management_system.settings')
django.setup()

from core.models import BusRoute, BusStop, User
from datetime import time
from decimal import Decimal

print('Creating Bangalore bus routes with SJB as home stop...\n')

# Get available drivers
drivers = User.objects.filter(role='driver')

# Route 1: Whitefield - Electronic City - SJB
route1, created = BusRoute.objects.get_or_create(
    route_number='SJB-WF-EC',
    defaults={
        'name': 'Whitefield - Electronic City Route',
        'bus_number': 'KA-01-AB-1234',
        'capacity': 40,
        'departure_time': time(6, 30),
        'arrival_time': time(8, 30),
        'driver': drivers[0] if drivers.exists() else None,
        'status': 'active',
        'description': 'Route covering Whitefield, Marathahalli, HSR Layout, Electronic City, Bommanahalli'
    }
)
print(f'Route 1: {route1.route_number} - {route1.name} ({"Created" if created else "Already exists"})')

# Add stops for Route 1
stops_route1 = [
    {'stop_name': 'Whitefield Bus Stand', 'pickup_time': time(6, 30), 'distance': 28.5, 'fare': 3500.00},
    {'stop_name': 'ITPL Main Gate', 'pickup_time': time(6, 40), 'distance': 26.0, 'fare': 3300.00},
    {'stop_name': 'Marathahalli Bridge', 'pickup_time': time(6, 50), 'distance': 22.0, 'fare': 3000.00},
    {'stop_name': 'HSR Layout Sector 1', 'pickup_time': time(7, 5), 'distance': 16.5, 'fare': 2500.00},
    {'stop_name': 'Electronic City Phase 1', 'pickup_time': time(7, 20), 'distance': 12.0, 'fare': 2000.00},
    {'stop_name': 'Bommanahalli Metro Station', 'pickup_time': time(7, 35), 'distance': 8.5, 'fare': 1500.00},
    {'stop_name': 'SJB Institute of Technology', 'pickup_time': time(7, 50), 'distance': 0.0, 'fare': 0.00},
]

for index, stop_data in enumerate(stops_route1, start=1):
    stop, created = BusStop.objects.get_or_create(
        route=route1,
        stop_name=stop_data['stop_name'],
        defaults={
            'stop_order': index,
            'pickup_time': stop_data['pickup_time'],
            'distance_from_sjb': Decimal(str(stop_data['distance'])),
            'base_fare': Decimal(str(stop_data['fare']))
        }
    )
    if created:
        print(f'  ✓ Added stop: {stop.stop_name}')

# Route 2: Banashankari - JP Nagar - SJB
route2, created = BusRoute.objects.get_or_create(
    route_number='SJB-BS-JP',
    defaults={
        'name': 'Banashankari - JP Nagar Route',
        'bus_number': 'KA-01-CD-5678',
        'capacity': 40,
        'departure_time': time(6, 45),
        'arrival_time': time(8, 30),
        'driver': drivers[1] if drivers.count() > 1 else (drivers[0] if drivers.exists() else None),
        'status': 'active',
        'description': 'Route covering Banashankari, Jayanagar, JP Nagar, BTM Layout'
    }
)
print(f'\nRoute 2: {route2.route_number} - {route2.name} ({"Created" if created else "Already exists"})')

# Add stops for Route 2
stops_route2 = [
    {'stop_name': 'Banashankari Bus Terminal', 'pickup_time': time(6, 45), 'distance': 18.0, 'fare': 2800.00},
    {'stop_name': 'South End Circle', 'pickup_time': time(6, 55), 'distance': 15.5, 'fare': 2500.00},
    {'stop_name': 'Jayanagar 4th Block', 'pickup_time': time(7, 5), 'distance': 13.0, 'fare': 2200.00},
    {'stop_name': 'JP Nagar Metro Station', 'pickup_time': time(7, 15), 'distance': 10.5, 'fare': 1800.00},
    {'stop_name': 'BTM Layout 1st Stage', 'pickup_time': time(7, 30), 'distance': 7.0, 'fare': 1400.00},
    {'stop_name': 'Arekere Gate', 'pickup_time': time(7, 40), 'distance': 4.5, 'fare': 1000.00},
    {'stop_name': 'SJB Institute of Technology', 'pickup_time': time(7, 50), 'distance': 0.0, 'fare': 0.00},
]

for index, stop_data in enumerate(stops_route2, start=1):
    stop, created = BusStop.objects.get_or_create(
        route=route2,
        stop_name=stop_data['stop_name'],
        defaults={
            'stop_order': index,
            'pickup_time': stop_data['pickup_time'],
            'distance_from_sjb': Decimal(str(stop_data['distance'])),
            'base_fare': Decimal(str(stop_data['fare']))
        }
    )
    if created:
        print(f'  ✓ Added stop: {stop.stop_name}')

# Route 3: Yelahanka - Hebbal - SJB
route3, created = BusRoute.objects.get_or_create(
    route_number='SJB-YL-HB',
    defaults={
        'name': 'Yelahanka - Hebbal Route',
        'bus_number': 'KA-01-EF-9012',
        'capacity': 40,
        'departure_time': time(6, 20),
        'arrival_time': time(8, 30),
        'driver': None,  # No driver assigned yet
        'status': 'active',
        'description': 'Route covering Yelahanka, Hebbal, RT Nagar, Yeshwanthpur, Malleshwaram'
    }
)
print(f'\nRoute 3: {route3.route_number} - {route3.name} ({"Created" if created else "Already exists"})')

# Add stops for Route 3
stops_route3 = [
    {'stop_name': 'Yelahanka New Town', 'pickup_time': time(6, 20), 'distance': 32.0, 'fare': 4000.00},
    {'stop_name': 'Hebbal Flyover', 'pickup_time': time(6, 35), 'distance': 26.5, 'fare': 3500.00},
    {'stop_name': 'RT Nagar', 'pickup_time': time(6, 45), 'distance': 23.0, 'fare': 3200.00},
    {'stop_name': 'Yeshwanthpur Metro', 'pickup_time': time(6, 55), 'distance': 19.5, 'fare': 2800.00},
    {'stop_name': 'Malleshwaram 18th Cross', 'pickup_time': time(7, 10), 'distance': 16.0, 'fare': 2400.00},
    {'stop_name': 'Rajajinagar', 'pickup_time': time(7, 20), 'distance': 13.5, 'fare': 2000.00},
    {'stop_name': 'Majestic Bus Stand', 'pickup_time': time(7, 35), 'distance': 9.0, 'fare': 1500.00},
    {'stop_name': 'SJB Institute of Technology', 'pickup_time': time(7, 50), 'distance': 0.0, 'fare': 0.00},
]

for index, stop_data in enumerate(stops_route3, start=1):
    stop, created = BusStop.objects.get_or_create(
        route=route3,
        stop_name=stop_data['stop_name'],
        defaults={
            'stop_order': index,
            'pickup_time': stop_data['pickup_time'],
            'distance_from_sjb': Decimal(str(stop_data['distance'])),
            'base_fare': Decimal(str(stop_data['fare']))
        }
    )
    if created:
        print(f'  ✓ Added stop: {stop.stop_name}')

# Route 4: Koramangala - Indiranagar - SJB
route4, created = BusRoute.objects.get_or_create(
    route_number='SJB-KR-IN',
    defaults={
        'name': 'Koramangala - Indiranagar Route',
        'bus_number': 'KA-01-GH-3456',
        'capacity': 40,
        'departure_time': time(6, 50),
        'arrival_time': time(8, 30),
        'driver': None,  # No driver assigned yet
        'status': 'active',
        'description': 'Route covering Koramangala, Indiranagar, Domlur, Ejipura, BTM Layout'
    }
)
print(f'\nRoute 4: {route4.route_number} - {route4.name} ({"Created" if created else "Already exists"})')

# Add stops for Route 4
stops_route4 = [
    {'stop_name': 'Koramangala Sony Signal', 'pickup_time': time(6, 50), 'distance': 14.5, 'fare': 2200.00},
    {'stop_name': 'Indiranagar 100 Feet Road', 'pickup_time': time(7, 0), 'distance': 12.0, 'fare': 2000.00},
    {'stop_name': 'Domlur Bus Stop', 'pickup_time': time(7, 10), 'distance': 10.0, 'fare': 1700.00},
    {'stop_name': 'Ejipura Signal', 'pickup_time': time(7, 20), 'distance': 8.0, 'fare': 1400.00},
    {'stop_name': 'Vivek Nagar', 'pickup_time': time(7, 30), 'distance': 6.0, 'fare': 1100.00},
    {'stop_name': 'BTM Layout 2nd Stage', 'pickup_time': time(7, 40), 'distance': 3.5, 'fare': 800.00},
    {'stop_name': 'SJB Institute of Technology', 'pickup_time': time(7, 50), 'distance': 0.0, 'fare': 0.00},
]

for index, stop_data in enumerate(stops_route4, start=1):
    stop, created = BusStop.objects.get_or_create(
        route=route4,
        stop_name=stop_data['stop_name'],
        defaults={
            'stop_order': index,
            'pickup_time': stop_data['pickup_time'],
            'distance_from_sjb': Decimal(str(stop_data['distance'])),
            'base_fare': Decimal(str(stop_data['fare']))
        }
    )
    if created:
        print(f'  ✓ Added stop: {stop.stop_name}')
        print(f'  ✓ Added stop: {stop.stop_name}')

print('\n' + '='*60)
print('✅ All 4 Bangalore routes created successfully!')
print('='*60)
print('\nRoute Summary:')
print(f'1. {route1.route_number}: {route1.name} ({BusStop.objects.filter(route=route1).count()} stops)')
print(f'2. {route2.route_number}: {route2.name} ({BusStop.objects.filter(route=route2).count()} stops)')
print(f'3. {route3.route_number}: {route3.name} ({BusStop.objects.filter(route=route3).count()} stops)')
print(f'4. {route4.route_number}: {route4.name} ({BusStop.objects.filter(route=route4).count()} stops)')
print('\nAll routes destination: SJB Institute of Technology')
print('Status: Active and ready for student registration')
