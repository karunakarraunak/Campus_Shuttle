from core.models import User, BusRoute

# Get drivers
drivers = User.objects.filter(role='driver').order_by('emp_no')

if drivers.count() >= 2:
    driver1 = drivers[0]  # EMP101
    driver2 = drivers[1]  # EMP102
    
    # Get routes
    route1 = BusRoute.objects.get(route_number='R01')  # North
    route2 = BusRoute.objects.get(route_number='R02')  # East
    
    # Assign drivers
    route1.driver = driver1
    route1.save()
    
    route2.driver = driver2
    route2.save()
    
    print(f"✅ Assigned {driver1.get_full_name()} ({driver1.emp_no}) to {route1.name}")
    print(f"✅ Assigned {driver2.get_full_name()} ({driver2.emp_no}) to {route2.name}")
    print("\n📋 Routes R03 and R04 are unassigned and available for assignment.")
else:
    print("❌ Not enough drivers found. Please create at least 2 drivers.")
