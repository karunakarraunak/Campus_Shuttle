from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import time, date, timedelta
from core.models import BusRoute, BusStop, User
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populate bus routes with 4 organized routes covering Bangalore areas'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating Bangalore bus routes...'))
        
        # Clear existing routes and stops
        BusStop.objects.all().delete()
        BusRoute.objects.all().delete()
        
        # Get drivers (if available)
        drivers = list(User.objects.filter(role='driver'))
        
        # Route 1: North Bangalore Route
        route1 = BusRoute.objects.create(
            name='North Bangalore Route',
            route_number='R01',
            description='Covering Hebbal, Yelahanka, and surrounding areas',
            bus_number='KA-01-AB-1234',
            capacity=45,
            driver=drivers[0] if len(drivers) > 0 else None,
            status='active',
            departure_time=time(7, 30),
            arrival_time=time(9, 0)
        )
        
        route1_stops = [
            {'name': 'Yelahanka New Town', 'distance': 18.5, 'time': time(7, 0), 'fare': Decimal('2800.00')},
            {'name': 'Yelahanka Old Town', 'distance': 17.2, 'time': time(7, 8), 'fare': Decimal('2700.00')},
            {'name': 'Jakkur Aerodrome', 'distance': 15.8, 'time': time(7, 15), 'fare': Decimal('2600.00')},
            {'name': 'Hebbal', 'distance': 14.2, 'time': time(7, 22), 'fare': Decimal('2500.00')},
            {'name': 'Manyata Tech Park', 'distance': 13.5, 'time': time(7, 28), 'fare': Decimal('2400.00')},
            {'name': 'HBR Layout', 'distance': 12.0, 'time': time(7, 35), 'fare': Decimal('2300.00')},
            {'name': 'Kalyan Nagar', 'distance': 10.5, 'time': time(7, 42), 'fare': Decimal('2200.00')},
            {'name': 'HRBR Layout', 'distance': 9.2, 'time': time(7, 48), 'fare': Decimal('2100.00')},
            {'name': 'Banaswadi', 'distance': 8.0, 'time': time(7, 54), 'fare': Decimal('2000.00')},
            {'name': 'Kacharakanahalli', 'distance': 6.5, 'time': time(8, 0), 'fare': Decimal('1800.00')},
            {'name': 'SJB Institute of Technology', 'distance': 0.0, 'time': time(8, 15), 'fare': Decimal('0.00')},
        ]
        
        for idx, stop in enumerate(route1_stops, 1):
            BusStop.objects.create(
                route=route1,
                stop_name=stop['name'],
                stop_order=idx,
                distance_from_sjb=stop['distance'],
                pickup_time=stop['time'],
                base_fare=stop['fare']
            )
        
        # Route 2: East Bangalore Route
        route2 = BusRoute.objects.create(
            name='East Bangalore Route',
            route_number='R02',
            description='Covering Whitefield, Marathahalli, and surrounding areas',
            bus_number='KA-01-CD-5678',
            capacity=40,
            driver=drivers[1] if len(drivers) > 1 else None,
            status='active',
            departure_time=time(7, 45),
            arrival_time=time(9, 15)
        )
        
        route2_stops = [
            {'name': 'Whitefield', 'distance': 22.0, 'time': time(7, 0), 'fare': Decimal('3200.00')},
            {'name': 'ITPL Main Gate', 'distance': 20.5, 'time': time(7, 10), 'fare': Decimal('3100.00')},
            {'name': 'Marathahalli Bridge', 'distance': 18.0, 'time': time(7, 20), 'fare': Decimal('2900.00')},
            {'name': 'Kundalahalli', 'distance': 16.5, 'time': time(7, 28), 'fare': Decimal('2800.00')},
            {'name': 'Brookefield', 'distance': 15.0, 'time': time(7, 35), 'fare': Decimal('2700.00')},
            {'name': 'HAL Airport', 'distance': 13.2, 'time': time(7, 43), 'fare': Decimal('2600.00')},
            {'name': 'Indiranagar', 'distance': 11.5, 'time': time(7, 52), 'fare': Decimal('2400.00')},
            {'name': 'Domlur', 'distance': 10.0, 'time': time(8, 0), 'fare': Decimal('2300.00')},
            {'name': 'Old Airport Road', 'distance': 8.5, 'time': time(8, 7), 'fare': Decimal('2100.00')},
            {'name': 'Binnamangala', 'distance': 6.0, 'time': time(8, 15), 'fare': Decimal('1900.00')},
            {'name': 'SJB Institute of Technology', 'distance': 0.0, 'time': time(8, 30), 'fare': Decimal('0.00')},
        ]
        
        for idx, stop in enumerate(route2_stops, 1):
            BusStop.objects.create(
                route=route2,
                stop_name=stop['name'],
                stop_order=idx,
                distance_from_sjb=stop['distance'],
                pickup_time=stop['time'],
                base_fare=stop['fare']
            )
        
        # Route 3: South Bangalore Route
        route3 = BusRoute.objects.create(
            name='South Bangalore Route',
            route_number='R03',
            description='Covering Banashankari, BTM, Jayanagar and surrounding areas',
            bus_number='KA-01-EF-9012',
            capacity=42,
            driver=None,  # No driver assigned yet
            status='active',
            departure_time=time(7, 15),
            arrival_time=time(8, 45)
        )
        
        route3_stops = [
            {'name': 'Banashankari', 'distance': 16.5, 'time': time(6, 45), 'fare': Decimal('2700.00')},
            {'name': 'JP Nagar 7th Phase', 'distance': 15.0, 'time': time(6, 52), 'fare': Decimal('2600.00')},
            {'name': 'BTM Layout', 'distance': 13.5, 'time': time(7, 0), 'fare': Decimal('2500.00')},
            {'name': 'Jayanagar 4th Block', 'distance': 12.0, 'time': time(7, 8), 'fare': Decimal('2400.00')},
            {'name': 'Lalbagh Main Gate', 'distance': 10.5, 'time': time(7, 16), 'fare': Decimal('2300.00')},
            {'name': 'National College', 'distance': 9.0, 'time': time(7, 23), 'fare': Decimal('2200.00')},
            {'name': 'Basavanagudi', 'distance': 8.0, 'time': time(7, 29), 'fare': Decimal('2100.00')},
            {'name': 'Majestic', 'distance': 6.5, 'time': time(7, 37), 'fare': Decimal('2000.00')},
            {'name': 'Shivajinagar', 'distance': 4.5, 'time': time(7, 45), 'fare': Decimal('1800.00')},
            {'name': 'Richmond Circle', 'distance': 3.0, 'time': time(7, 52), 'fare': Decimal('1600.00')},
            {'name': 'SJB Institute of Technology', 'distance': 0.0, 'time': time(8, 0), 'fare': Decimal('0.00')},
        ]
        
        for idx, stop in enumerate(route3_stops, 1):
            BusStop.objects.create(
                route=route3,
                stop_name=stop['name'],
                stop_order=idx,
                distance_from_sjb=stop['distance'],
                pickup_time=stop['time'],
                base_fare=stop['fare']
            )
        
        # Route 4: West Bangalore Route
        route4 = BusRoute.objects.create(
            name='West Bangalore Route',
            route_number='R04',
            description='Covering Rajajinagar, Malleshwaram, Yeshwanthpur and surrounding areas',
            bus_number='KA-01-GH-3456',
            capacity=38,
            driver=None,
            status='active',
            departure_time=time(7, 30),
            arrival_time=time(8, 50)
        )
        
        route4_stops = [
            {'name': 'Yeshwanthpur', 'distance': 14.0, 'time': time(7, 0), 'fare': Decimal('2600.00')},
            {'name': 'Sandal Soap Factory', 'distance': 12.8, 'time': time(7, 7), 'fare': Decimal('2500.00')},
            {'name': 'Peenya Industrial Area', 'distance': 11.5, 'time': time(7, 14), 'fare': Decimal('2400.00')},
            {'name': 'Jalahalli', 'distance': 10.0, 'time': time(7, 21), 'fare': Decimal('2300.00')},
            {'name': 'Mathikere', 'distance': 8.8, 'time': time(7, 28), 'fare': Decimal('2200.00')},
            {'name': 'Malleshwaram', 'distance': 7.5, 'time': time(7, 35), 'fare': Decimal('2100.00')},
            {'name': 'Rajajinagar', 'distance': 6.2, 'time': time(7, 42), 'fare': Decimal('2000.00')},
            {'name': 'Mahalaxmi Layout', 'distance': 5.0, 'time': time(7, 49), 'fare': Decimal('1900.00')},
            {'name': 'Nagarbhavi', 'distance': 3.5, 'time': time(7, 56), 'fare': Decimal('1700.00')},
            {'name': 'Rajarajeshwari Nagar', 'distance': 2.0, 'time': time(8, 3), 'fare': Decimal('1500.00')},
            {'name': 'SJB Institute of Technology', 'distance': 0.0, 'time': time(8, 15), 'fare': Decimal('0.00')},
        ]
        
        for idx, stop in enumerate(route4_stops, 1):
            BusStop.objects.create(
                route=route4,
                stop_name=stop['name'],
                stop_order=idx,
                distance_from_sjb=stop['distance'],
                pickup_time=stop['time'],
                base_fare=stop['fare']
            )
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully created 4 bus routes!'))
        self.stdout.write(self.style.SUCCESS(f'   - Route 1 (North): {route1.get_total_stops()} stops'))
        self.stdout.write(self.style.SUCCESS(f'   - Route 2 (East): {route2.get_total_stops()} stops'))
        self.stdout.write(self.style.SUCCESS(f'   - Route 3 (South): {route3.get_total_stops()} stops'))
        self.stdout.write(self.style.SUCCESS(f'   - Route 4 (West): {route4.get_total_stops()} stops'))
        self.stdout.write(self.style.SUCCESS(f'\n📍 All routes end at: SJB Institute of Technology'))
