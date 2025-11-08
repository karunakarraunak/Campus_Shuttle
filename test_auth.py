import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_management_system.settings')
django.setup()

from django.contrib.auth import authenticate

print('Testing authentication...\n')

# Test admin
user = authenticate(username='admin', password='admin123')
print(f'Admin (username: admin): {"SUCCESS ✅" if user else "FAILED ❌"}')

# Test students
user2 = authenticate(username='CS001', password='student123')
print(f'Student (USN: CS001): {"SUCCESS ✅" if user2 else "FAILED ❌"}')

user3 = authenticate(username='CS002', password='student123')
print(f'Student (USN: CS002): {"SUCCESS ✅" if user3 else "FAILED ❌"}')

# Test drivers
user4 = authenticate(username='EMP101', password='driver123')
print(f'Driver (Employee: EMP101): {"SUCCESS ✅" if user4 else "FAILED ❌"}')

user5 = authenticate(username='EMP102', password='driver123')
print(f'Driver (Employee: EMP102): {"SUCCESS ✅" if user5 else "FAILED ❌"}')

print('\n' + '='*50)
if all([user, user2, user3, user4, user5]):
    print('✅ All authentication tests PASSED!')
    print('You can now login at: http://localhost:8000/login/')
else:
    print('❌ Some authentication tests FAILED')
    print('Please check the credentials')
