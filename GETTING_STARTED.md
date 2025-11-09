# 🚀 Getting Started with CampusShuttle

This guide will walk you through setting up and running the CampusShuttle Transport Management System from scratch.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Initial Setup](#initial-setup)
- [Database Setup](#database-setup)
- [Creating Your First Admin User](#creating-your-first-admin-user)
- [Creating Test Users](#creating-test-users)
- [Setting Up Routes and Stops](#setting-up-routes-and-stops)
- [Testing the System](#testing-the-system)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10+** installed on your system
- **Git** for version control
- Basic knowledge of Django framework
- A code editor (VS Code, PyCharm, etc.)

---

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/karunakarraunak/Campus_Shuttle.git
cd Campus_Shuttle
```

### 2. Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Your terminal should show `(venv)` prefix, indicating the virtual environment is active.

---

## Database Setup

### 1. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the SQLite database and all necessary tables.

### 2. Verify Database Creation

You should see a new file: `db.sqlite3` in your project root.

---

## Creating Your First Admin User

### 1. Create Superuser

Run the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

**Example:**
```
Username: admin
Email address: admin@campusshuttle.com
Password: ********
Password (again): ********
Superuser created successfully.
```

**💡 Tips:**
- Choose a strong password (minimum 8 characters)
- Remember these credentials - you'll need them to access the admin panel
- Email is optional but recommended

### 2. Start the Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### 3. Access Admin Panel

1. Open your browser and navigate to: `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. You should see the Django administration dashboard

---

## Creating Test Users

### Option 1: Via Admin Panel (Recommended for Beginners)

#### Create an Admin User

1. In admin panel, click **Users** → **Add User**
2. Enter username (e.g., `admin_user`)
3. Enter password (twice)
4. Click **Save and continue editing**
5. In the user form:
   - **First name**: John
   - **Last name**: Admin
   - **Email**: john.admin@example.com
   - **Role**: Select `Admin`
   - **Phone number**: +91 9876543210
6. Click **Save**

#### Create Student Users

1. Click **Users** → **Add User**
2. Username: `CS001`
3. Set password
4. Click **Save and continue editing**
5. Fill in:
   - **First name**: Aditya
   - **Last name**: Sharma
   - **Email**: aditya@example.com
   - **Role**: `Student`
   - **Phone number**: +91 9876543211
   - **Address**: Bangalore, India
6. Click **Save**

Repeat for more students (CS002, CS003, etc.)

#### Create Driver Users

1. Click **Users** → **Add User**
2. Username: `EMP101`
3. Set password
4. Click **Save and continue editing**
5. Fill in:
   - **First name**: Vijay
   - **Last name**: Kumar
   - **Email**: vijay.kumar@example.com
   - **Role**: `Driver`
   - **Phone number**: +91 9876543220
   - **Address**: Bangalore, India
6. Click **Save**

Repeat for more drivers (EMP102, EMP103, etc.)

### Option 2: Using Django Shell (Advanced)

```bash
python manage.py shell
```

Then run:

```python
from core.models import User

# Create admin
admin = User.objects.create_user(
    username='admin_user',
    password='your_secure_password',
    first_name='John',
    last_name='Admin',
    email='admin@example.com',
    role='admin',
    phone_number='+91 9876543210'
)

# Create student
student = User.objects.create_user(
    username='CS001',
    password='your_secure_password',
    first_name='Aditya',
    last_name='Sharma',
    email='aditya@example.com',
    role='student',
    phone_number='+91 9876543211'
)

# Create driver
driver = User.objects.create_user(
    username='EMP101',
    password='your_secure_password',
    first_name='Vijay',
    last_name='Kumar',
    email='vijay@example.com',
    role='driver',
    phone_number='+91 9876543220'
)

print("✅ Users created successfully!")
```

Exit shell: Press `Ctrl + D` or type `exit()`

---

## Setting Up Routes and Stops

### Create a Bus Route

1. In admin panel, go to **Bus Routes** → **Add Bus Route**
2. Fill in the details:

| Field | Example Value |
|-------|---------------|
| **Name** | Whitefield - Electronic City Route |
| **Route number** | SJB-WF-EC |
| **Description** | Connects Whitefield to Electronic City via major tech parks |
| **Bus number** | KA01AB1234 |
| **Capacity** | 40 |
| **Driver** | Select EMP101 (Vijay Kumar) |
| **Status** | Active |
| **Departure time** | 08:00 AM |
| **Arrival time** | 09:30 AM |

3. Click **Save**

### Add Bus Stops

1. Go to **Bus Stops** → **Add Bus Stop**
2. Add stops in sequence:

**Stop 1:**
- Route: SJB-WF-EC
- Stop name: SJB Institute (Main Campus)
- Stop order: 1
- Pickup time: 08:00 AM
- Distance from SJB: 0 km
- Base fare: ₹0
- Latitude: 12.9716
- Longitude: 77.5946

**Stop 2:**
- Route: SJB-WF-EC
- Stop name: Whitefield Main Road
- Stop order: 2
- Pickup time: 08:15 AM
- Distance from SJB: 5 km
- Base fare: ₹20
- Latitude: 12.9698
- Longitude: 77.7500

**Stop 3:**
- Route: SJB-WF-EC
- Stop name: Electronic City
- Stop order: 3
- Pickup time: 08:45 AM
- Distance from SJB: 15 km
- Base fare: ₹50
- Latitude: 12.8456
- Longitude: 77.6603

Repeat for all stops along your route.

---

## Testing the System

### Test as Admin

1. Logout from superuser
2. Go to: `http://127.0.0.1:8000/login/`
3. Login with admin credentials (e.g., `admin_user`)
4. You should see:
   - Dashboard with statistics
   - All routes overview
   - User management options
   - Analytics

### Test as Student

1. Logout and login as student (e.g., `CS001`)
2. Test features:
   - **View Available Routes**: See all bus routes
   - **Register for Route**: Select a route and bus stop
   - **Track Bus**: View real-time location on map
   - **Submit Query**: Ask questions to admin

### Test as Driver

1. Logout and login as driver (e.g., `EMP101`)
2. Test features:
   - **View Assigned Route**: See your route details
   - **Share Location**: Click "Start Sharing Location"
   - **Browser Permission**: Allow location access when prompted
   - **Track Updates**: Location updates every 10 seconds

### Test GPS Tracking

**As Driver:**
1. Login and go to "Track Bus"
2. Click "Start Sharing Location"
3. Allow browser location permission
4. Status should show "Location sharing is ON"

**As Student:**
1. Login in a different browser/incognito window
2. Go to "Track Bus"
3. You should see the driver's bus location on the map
4. The marker updates automatically every 20 seconds

---

## Troubleshooting

### Issue: "No such table" Error

**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "Address already in use" Error

**Solution:**
Kill the process on port 8000:

**macOS/Linux:**
```bash
lsof -ti:8000 | xargs kill -9
```

**Windows:**
```bash
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

### Issue: Location Sharing Not Working

**Possible Causes:**
1. **Browser Permission**: Ensure location access is allowed
2. **HTTPS Required**: Some browsers require HTTPS for geolocation
3. **Localhost Works**: `http://127.0.0.1:8000` should work fine

**Solution:**
- Check browser console (F12) for errors
- Clear browser cache
- Try a different browser

### Issue: Can't Login After Creating User

**Solution:**
Check if you set a password:
```bash
python manage.py shell
```

```python
from core.models import User
user = User.objects.get(username='your_username')
user.set_password('new_password')
user.save()
```

### Issue: Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic
```

For development, ensure in `settings.py`:
```python
DEBUG = True
```

---

## Quick Reference Commands

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Create admin user
python manage.py createsuperuser

# Run tests
python manage.py test
```

---

## Next Steps

1. ✅ **Create More Routes**: Add routes for different areas
2. ✅ **Add More Stops**: Create comprehensive stop coverage
3. ✅ **Register Students**: Have students register for routes
4. ✅ **Test GPS Tracking**: Ensure real-time location works
5. ✅ **Explore Features**: Try notifications, queries, registration

---

## 📞 Need Help?

- **Documentation**: Check `README.md` for detailed information
- **Issues**: Report bugs on [GitHub Issues](https://github.com/karunakarraunak/Campus_Shuttle/issues)
- **Email**: Contact the development team

---

**Happy Coding! 🚀**

*Built with ❤️ using Django and Leaflet.js*
