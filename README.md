# 🚌 CampusShuttle - Transport Management System

A comprehensive, real-time campus transport management system built with Django, featuring GPS tracking, route management, and role-based access control.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents
- [Features](#-features)
- [Screenshots](#️-screenshots)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
  - [macOS Setup](#macos-setup)
  - [Windows Setup](#windows-setup)
- [Usage](#-usage)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Database Models](#️-database-models)
- [API Endpoints](#-api-endpoints)
- [Contributing](#-contributing)
- [Known Issues & Future Enhancements](#-known-issues--future-enhancements)
- [License](#-license)
- [Authors](#-authors)
- [Support](#-support)

## ✨ Features

### � Core Functionality
- **Real-time GPS Bus Tracking** - Track buses live using HTML5 Geolocation API with OpenStreetMap
- **Route Management** - 4 pre-configured Bangalore city routes with 29 bus stops
- **Student Registration** - Students can register for routes and select pickup points
- **Driver Location Sharing** - Drivers can share their live location
- **Admin Dashboard** - Complete oversight of routes, registrations, and users
- **Notifications System** - Broadcast and targeted notifications
- **Query Management** - Student queries with admin responses

### �🎨 Modern UI/UX
- Clean, minimalist design with gradient themes
- Fully responsive layout (mobile, tablet, desktop)
- Smooth animations and transitions
- Professional color scheme
- Interactive maps with Leaflet.js
- Real-time updates

### 👥 Role-Based Authentication
Three distinct user roles with specialized dashboards:

1. **👨‍💼 Admin**
   - Manage all routes and bus stops
   - Approve/reject student registrations
   - View all driver locations
   - Create notifications and announcements
   - Respond to student queries
   - Monitor system analytics
   - User management

2. **👨‍✈️ Driver**
   - Share real-time GPS location
   - View assigned route details
   - Track own location history
   - View route-specific notifications
   - Update availability status

3. **👨‍🎓 Student**
   - Browse available bus routes
   - Register for a route and select stop
   - Track registered bus in real-time
   - View pickup times and fares
   - Submit queries to admin
   - Receive notifications
   - View route details with interactive maps

### �️ Route Information
**4 Bangalore City Routes:**
1. **SJB-WF-EC** - Whitefield → Electronic City → SJB (7 stops, 28.5km)
2. **SJB-BS-JP** - Banashankari → JP Nagar → SJB (7 stops, 18km)
3. **SJB-YL-HB** - Yelahanka → Hebbal → SJB (8 stops, 32km)
4. **SJB-KR-IN** - Koramangala → Indiranagar → SJB (7 stops, 14.5km)

All routes end at **SJB Institute of Technology**

## 🖼️ Screenshots

*(Screenshots can be added here showing different dashboards and features)*

## 🛠️ Tech Stack

**Backend:**
- Django 5.2.8
- Python 3.12
- SQLite Database

**Frontend:**
- HTML5, CSS3, JavaScript
- Leaflet.js for maps
- OpenStreetMap tiles
- Responsive CSS Grid & Flexbox

**APIs & Libraries:**
- HTML5 Geolocation API
- Django REST Framework patterns
- AJAX for real-time updates

**Features:**
- Custom User Model with role-based permissions
- Real-time GPS tracking
- One-to-One driver-route assignment
- Migration-based database schema

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### macOS Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/karunakarraunak/Campus_Shuttle.git
   cd Campus_Shuttle
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create test users (optional):**
   ```bash
   # Admin user
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`

### Windows Setup

1. **Clone the repository:**
   ```cmd
   git clone https://github.com/karunakarraunak/Campus_Shuttle.git
   cd Campus_Shuttle
   ```

2. **Create a virtual environment:**
   ```cmd
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```cmd
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```cmd
   python manage.py migrate
   ```

6. **Create test users (optional):**
   ```cmd
   rem Admin user
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```cmd
   python manage.py runserver
   ```

8. **Access the application:**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📖 Usage

### First Time Setup

After installation, you'll need to:

1. **Create an admin account** using the createsuperuser command
2. **Add bus routes** via the Django admin panel (`/admin/`)
3. **Create test users** for students and drivers (or use test credentials below)

### Accessing Different Dashboards

- **Landing Page:** `http://127.0.0.1:8000/`
- **Login:** `http://127.0.0.1:8000/login/`
- **Sign Up:** `http://127.0.0.1:8000/signup/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Browse Routes:** `http://127.0.0.1:8000/routes/`
- **Track Bus:** `http://127.0.0.1:8000/track-bus/`

### Using GPS Tracking

**For Drivers:**
1. Login with driver credentials
2. Navigate to "Track Bus" section
3. Click "Start Sharing Location"
4. Allow browser location permissions
5. Your location will be shared in real-time

**For Students:**
1. Login with student credentials
2. Register for a route first (Browse Routes → Select Route → Register)
3. Navigate to "Track Bus" section
4. View your registered route driver's location on the map
5. Toggle "Auto-refresh" for live updates

**For Admins:**
1. Login with admin credentials
2. Navigate to "Track Bus" section
3. View all active driver locations simultaneously

## � Getting Started

### Step 1: Create Superuser

After setting up the project and running migrations, create an admin superuser:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- **Username**: Choose your admin username
- **Email**: Your email address (optional)
- **Password**: Choose a secure password
- **Confirm Password**: Re-enter the password

### Step 2: Access Admin Panel

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to the admin panel:
   ```
   http://127.0.0.1:8000/admin/
   ```

3. Login with your superuser credentials

### Step 3: Create Test Users

In the admin panel, create users for testing:

**Create an Admin User:**
1. Go to **Users** → **Add User**
2. Set username (e.g., `admin`)
3. Set password
4. Edit the user and set **Role** to `Admin`
5. Save

**Create Student Users:**
1. Go to **Users** → **Add User**
2. Set username (e.g., `CS001`, `CS002`)
3. Set password
4. Edit the user and set:
   - **Role**: `Student`
   - **First name**, **Last name**
   - **Email**, **Phone number**
5. Save

**Create Driver Users:**
1. Go to **Users** → **Add User**
2. Set username (e.g., `EMP101`, `EMP102`)
3. Set password
4. Edit the user and set:
   - **Role**: `Driver`
   - **First name**, **Last name**
   - **Phone number**
5. Save

### Step 4: Create Bus Routes

1. In admin panel, go to **Bus Routes** → **Add Bus Route**
2. Fill in route details:
   - Name (e.g., "Whitefield - Electronic City Route")
   - Route number (e.g., "SJB-WF-EC")
   - Bus number
   - Capacity
   - Departure time
   - Arrival time
3. Assign a driver to the route
4. Save

### Step 5: Add Bus Stops

1. Go to **Bus Stops** → **Add Bus Stop**
2. For each stop, enter:
   - Route (select from dropdown)
   - Stop name
   - Stop order (sequence number)
   - Pickup time
   - Base fare
   - Distance from SJB
   - GPS coordinates (latitude, longitude)
3. Save

### Step 6: Test the System

1. **Login as Admin** → View all routes, manage users, view analytics
2. **Login as Student** → Register for a route, track bus location
3. **Login as Driver** → Share location, view assigned route

### Quick Setup Script (Optional)

You can create test data programmatically:

```python
# create_test_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_management_system.settings')
django.setup()

from core.models import User, BusRoute, BusStop
from django.utils import timezone
from datetime import time, date

# Create users
admin = User.objects.create_user(username='admin', password='your_password', role='admin')
student = User.objects.create_user(username='student1', password='your_password', role='student')
driver = User.objects.create_user(username='driver1', password='your_password', role='driver')

# Create route
route = BusRoute.objects.create(
    name='Test Route',
    route_number='TR-001',
    bus_number='KA01AB1234',
    capacity=40,
    driver=driver,
    departure_time=time(8, 0),
    arrival_time=time(9, 30)
)

print("Test data created successfully!")
```

Run with: `python create_test_data.py`

**⚠️ Security Note:** Never commit passwords or sensitive credentials to your repository!

## 📁 Project Structure

```
Campus_Shuttle/
├── 📄 manage.py                      # Django management script
├── 📄 requirements.txt               # Python dependencies
├── 📄 README.md                      # Project documentation
├── 📄 GETTING_STARTED.md             # Step-by-step setup guide
├── 📄 .gitignore                     # Git ignore rules
│
├── 📂 core/                          # Main Django application
│   ├── 📂 migrations/                # Database migrations
│   ├── 📂 management/                # Custom management commands
│   │   └── 📂 commands/
│   │       └── populate_routes.py   # Route population script
│   │
│   ├── 📂 static/core/               # Static files (CSS, JS)
│   │   ├── 📂 css/
│   │   │   ├── style.css            # Landing page styles
│   │   │   ├── auth.css             # Authentication styles
│   │   │   └── dashboard.css        # Dashboard styles
│   │   └── 📂 js/
│   │       └── main.js              # JavaScript functionality
│   │
│   ├── 📂 templates/core/            # HTML templates
│   │   ├── base.html                # Base template
│   │   ├── landing.html             # Landing page
│   │   ├── login.html               # Login page
│   │   ├── signup.html              # Signup page
│   │   ├── dashboard_admin.html     # Admin dashboard
│   │   ├── dashboard_driver.html    # Driver dashboard
│   │   ├── dashboard_student.html   # Student dashboard
│   │   ├── routes_list.html         # Browse routes
│   │   ├── route_detail.html        # Individual route details
│   │   ├── register_route.html      # Route registration form
│   │   ├── my_registration.html     # Student's registration
│   │   ├── track_bus.html           # GPS tracking page
│   │   ├── notifications.html       # Notifications page
│   │   ├── create_notification.html # Create notification (admin)
│   │   ├── student_queries.html     # Student queries
│   │   ├── answer_query.html        # Answer query (admin)
│   │   └── edit_profile.html        # Edit user profile
│   │
│   ├── 📄 models.py                  # Database models
│   ├── 📄 views.py                   # View functions
│   ├── 📄 forms.py                   # Django forms
│   ├── 📄 urls.py                    # URL routing
│   ├── 📄 admin.py                   # Admin panel config
│   └── 📄 apps.py                    # App configuration
│
├── 📂 transport_management_system/  # Django project settings
│   ├── 📄 __init__.py
│   ├── 📄 settings.py               # Project settings
│   ├── 📄 urls.py                   # Root URL configuration
│   ├── 📄 wsgi.py                   # WSGI configuration
│   └── 📄 asgi.py                   # ASGI configuration
│
├── 📂 media/                         # User uploaded files (gitignored)
│   └── profiles/                    # Profile images
│
├── 📂 venv/                          # Virtual environment (gitignored)
└── 📄 db.sqlite3                     # SQLite database (gitignored)
```

## 🗄️ Database Models

**User Model (Custom):**
- Extended Django user with roles (admin, student, driver)
- Fields: username, email, first_name, last_name, role, phone, address, profile_image

**BusRoute:**
- Route information (name, route_number, bus_number, capacity)
- Driver assignment (OneToOne)
- Status (active, inactive, maintenance)
- Departure and arrival times

**BusStop:**
- Individual stops in a route
- Stop order, name, pickup time
- Distance from SJB, base fare
- GPS coordinates (latitude, longitude)

**RouteRegistration:**
- Student route enrollments
- Selected bus stop
- Status (pending, active, cancelled)
- Monthly fee calculation

**BusLocation:**
- Real-time GPS tracking
- Driver location history
- Latitude, longitude, speed, heading, accuracy
- Timestamp and active status

**Notification:**
- System-wide and route-specific notifications
- Title, message, notification_type
- Target routes and creation timestamp

**QuickQuery:**
- Student queries with admin responses
- Subject, description, response
- Status tracking and timestamps

## 🔌 API Endpoints

### GPS Tracking APIs

**Update Driver Location (POST):**
```
POST /api/update-location/
Body: {
  "latitude": float,
  "longitude": float,
  "speed": float (optional),
  "heading": float (optional),
  "accuracy": float (optional)
}
Response: {"status": "success", "message": "Location updated"}
```

**Get Bus Locations (GET):**
```
GET /api/get-locations/
Response: {
  "locations": [
    {
      "driver_id": int,
      "driver_name": str,
      "route_number": str,
      "latitude": float,
      "longitude": float,
      "speed": float,
      "heading": float,
      "accuracy": float,
      "timestamp": str
    }
  ]
}
```

### Main Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | Landing | Home page |
| `/login/` | Login | User authentication |
| `/signup/` | Signup | User registration |
| `/logout/` | Logout | User logout |
| `/dashboard/` | Dashboard | Role-based dashboard |
| `/routes/` | Routes List | Browse available routes |
| `/routes/<id>/` | Route Detail | View specific route |
| `/routes/register/` | Register Route | Student registration |
| `/my-registration/` | My Registration | View student's registration |
| `/track-bus/` | Track Bus | Real-time GPS tracking |
| `/notifications/` | Notifications | View notifications |
| `/queries/` | Student Queries | Submit and view queries |
| `/profile/edit/` | Edit Profile | Update user profile |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Coding Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes
- Test your changes before submitting

## 🐛 Known Issues & Future Enhancements

**Known Issues:**
- GPS accuracy depends on device and browser
- Auto-refresh may consume more battery on mobile

**Future Enhancements:**
- [ ] Mobile app (React Native/Flutter)
- [ ] SMS notifications for route updates
- [ ] Payment gateway integration
- [ ] Route optimization algorithms
- [ ] Driver attendance tracking
- [ ] Student attendance via QR code
- [ ] Analytics dashboard with charts
- [ ] Export reports (PDF/Excel)
- [ ] Multi-language support
- [ ] Dark mode theme

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Karunakar Raunak** - *Initial work* - [karunakarraunak](https://github.com/karunakarraunak)

## 🙏 Acknowledgments

- Django framework and community
- OpenStreetMap for map tiles
- Leaflet.js for interactive maps
- Inter font family by Rasmus Andersson
- All contributors and testers

## 📞 Support

For support, email [your-email@example.com] or open an issue on GitHub.

## 🌟 Show your support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ using Django and Leaflet.js**
