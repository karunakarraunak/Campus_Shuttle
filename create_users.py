from core.models import User

# Clear existing users (optional)
User.objects.all().delete()

# Create 2 students
student1 = User.objects.create_user(
    username='CS001',
    usn='CS001',
    first_name='Rahul',
    last_name='Sharma',
    email='rahul.sharma@campusshuttle.edu',
    phone_number='9876543210',
    gender='male',
    role='student',
    password='student123'
)

student2 = User.objects.create_user(
    username='CS002',
    usn='CS002',
    first_name='Priya',
    last_name='Patel',
    email='priya.patel@campusshuttle.edu',
    phone_number='9876543211',
    gender='female',
    role='student',
    password='student123'
)

# Create 2 drivers
driver1 = User.objects.create_user(
    username='EMP101',
    emp_no='EMP101',
    first_name='Vijay',
    last_name='Kumar',
    email='vijay.kumar@campusshuttle.edu',
    phone_number='9876543212',
    gender='male',
    role='driver',
    password='driver123'
)

driver2 = User.objects.create_user(
    username='EMP102',
    emp_no='EMP102',
    first_name='Anjali',
    last_name='Singh',
    email='anjali.singh@campusshuttle.edu',
    phone_number='9876543213',
    gender='female',
    role='driver',
    password='driver123'
)

# Create 1 admin
admin1 = User.objects.create_user(
    username='admin',
    email='admin@campusshuttle.edu',
    role='admin',
    is_staff=True,
    is_superuser=True,
    password='admin123'
)

print("✅ All dummy accounts created successfully!")
print("\nCreated accounts:")
print(f"- 2 Students: {student1.usn}, {student2.usn}")
print(f"- 2 Drivers: {driver1.emp_no}, {driver2.emp_no}")
print(f"- 1 Admin: {admin1.username}")
