import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_management_system.settings')
django.setup()

from core.models import User

print('Creating test accounts from test_credentials.html...\n')

# ========================================
# ADMIN ACCOUNT
# ========================================
admin, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@campusshuttle.com',
        'first_name': 'System',
        'last_name': 'Administrator',
        'role': 'admin',
        'is_staff': True,
        'is_superuser': True,
    }
)
admin.role = 'admin'
admin.is_staff = True
admin.is_superuser = True
admin.set_password('admin123')
admin.save()
print('⚙️  ADMIN ACCOUNT')
print('   Username: admin')
print('   Password: admin123')
print('   Status: ' + ('Created' if created else 'Updated'))

# ========================================
# STUDENT ACCOUNTS
# ========================================
print('\n🎓 STUDENT ACCOUNTS')

# Student 1: Aditya Sharma
student1, created = User.objects.get_or_create(
    username='CS001',
    defaults={
        'email': 'aditya.sharma@student.campusshuttle.com',
        'first_name': 'Aditya',
        'last_name': 'Sharma',
        'role': 'student',
        'usn': 'CS001',
    }
)
student1.role = 'student'
student1.usn = 'CS001'
student1.set_password('student123')
student1.save()
print('   1. Aditya Sharma')
print('      USN: CS001')
print('      Password: student123')
print('      Status: ' + ('Created' if created else 'Updated'))

# Student 2: Priya Patel
student2, created = User.objects.get_or_create(
    username='CS002',
    defaults={
        'email': 'priya.patel@student.campusshuttle.com',
        'first_name': 'Priya',
        'last_name': 'Patel',
        'role': 'student',
        'usn': 'CS002',
    }
)
student2.role = 'student'
student2.usn = 'CS002'
student2.set_password('student123')
student2.save()
print('   2. Priya Patel')
print('      USN: CS002')
print('      Password: student123')
print('      Status: ' + ('Created' if created else 'Updated'))

# ========================================
# DRIVER ACCOUNTS
# ========================================
print('\n🚌 DRIVER ACCOUNTS')

# Driver 1: Vijay Kumar
driver1, created = User.objects.get_or_create(
    username='EMP101',
    defaults={
        'email': 'vijay.kumar@driver.campusshuttle.com',
        'first_name': 'Vijay',
        'last_name': 'Kumar',
        'role': 'driver',
        'emp_no': 'EMP101',
    }
)
driver1.role = 'driver'
driver1.emp_no = 'EMP101'
driver1.set_password('driver123')
driver1.save()
print('   1. Vijay Kumar')
print('      Employee No: EMP101')
print('      Password: driver123')
print('      Status: ' + ('Created' if created else 'Updated'))

# Driver 2: Anjali Singh
driver2, created = User.objects.get_or_create(
    username='EMP102',
    defaults={
        'email': 'anjali.singh@driver.campusshuttle.com',
        'first_name': 'Anjali',
        'last_name': 'Singh',
        'role': 'driver',
        'emp_no': 'EMP102',
    }
)
driver2.role = 'driver'
driver2.emp_no = 'EMP102'
driver2.set_password('driver123')
driver2.save()
print('   2. Anjali Singh')
print('      Employee No: EMP102')
print('      Password: driver123')
print('      Status: ' + ('Created' if created else 'Updated'))

print('\n' + '='*50)
print('✅ All test accounts created successfully!')
print('='*50)
print('\n🌐 Access the system at: http://localhost:8000/login/')
print('📄 View credentials at: file:///Users/apple/Desktop/Workspace/Transport_Management_System/test_credentials.html')
