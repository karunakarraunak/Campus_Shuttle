# Transport Management System

A modern, role-based transport management system built with Django.

## Features

### 🎨 Modern UI/UX
- Clean, minimalist design
- Fully responsive layout
- Smooth animations and transitions
- Professional color scheme

### 👥 Role-Based Authentication
Three distinct user roles with specialized dashboards:

1. **Admin** 👨‍💼
   - Manage users, fleet, and operations
   - View system analytics
   - Monitor active shipments
   - Generate reports

2. **Driver** 🚗
   - Track deliveries
   - View assigned routes
   - Update delivery status
   - Monitor performance metrics

3. **Student** 🎓
   - View transport schedule
   - Track bus location
   - Manage bookings
   - Check balance and payments

### 📱 Pages Included
- **Landing Page** - Modern homepage with features showcase
- **Login Page** - User authentication
- **Sign Up Page** - New user registration with role selection
- **Dashboard** - Role-specific dashboards for each user type

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- virtualenv

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/apple/Desktop/Workspace/Transport_Management_System
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Run migrations (already completed):**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Landing Page: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/login/
   - Sign Up: http://127.0.0.1:8000/signup/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
Transport_Management_System/
├── core/                          # Main application
│   ├── migrations/               # Database migrations
│   ├── static/core/              # Static files
│   │   ├── css/
│   │   │   ├── style.css        # Landing page styles
│   │   │   ├── auth.css         # Authentication pages styles
│   │   │   └── dashboard.css    # Dashboard styles
│   │   └── js/
│   │       └── main.js          # JavaScript functionality
│   ├── templates/core/          # HTML templates
│   │   ├── landing.html         # Landing page
│   │   ├── login.html           # Login page
│   │   ├── signup.html          # Signup page
│   │   ├── dashboard_admin.html # Admin dashboard
│   │   ├── dashboard_driver.html# Driver dashboard
│   │   └── dashboard_student.html# Student dashboard
│   ├── admin.py                 # Admin configuration
│   ├── forms.py                 # Forms (Login, SignUp)
│   ├── models.py                # Custom User model
│   ├── urls.py                  # URL routing
│   └── views.py                 # View functions
├── transport_management_system/ # Project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── manage.py                    # Django management script
└── venv/                        # Virtual environment
```

## Technologies Used

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default)
- **Image Processing:** Pillow
- **Font:** Inter (Google Fonts)

## User Model

Custom user model with the following fields:
- Username
- Email
- First Name
- Last Name
- Phone Number (optional)
- Profile Image (optional)
- Role (Admin, Driver, Student)
- Created At
- Updated At

## Usage

### Creating a New User

1. Navigate to the signup page
2. Fill in all required information
3. Select your role (Admin, Driver, or Student)
4. Submit the form
5. You'll be automatically logged in and redirected to your role-specific dashboard

### Logging In

1. Navigate to the login page
2. Enter your username and password
3. Click "Sign In"
4. You'll be redirected to your dashboard based on your role

### Dashboard Features

Each dashboard includes:
- Statistics cards with key metrics
- Role-specific functionality
- Quick actions panel
- Navigation sidebar
- User profile display

## Customization

### Adding New Features

1. **Add new models** in `core/models.py`
2. **Create forms** in `core/forms.py`
3. **Add views** in `core/views.py`
4. **Configure URLs** in `core/urls.py`
5. **Create templates** in `core/templates/core/`
6. **Add styles** in `core/static/core/css/`

### Styling

All CSS is organized into three main files:
- `style.css` - Landing page styling
- `auth.css` - Login/Signup pages styling
- `dashboard.css` - Dashboard styling

CSS variables are used for easy theme customization.

## Next Steps

Potential enhancements:
- [ ] Real-time GPS tracking
- [ ] Payment integration
- [ ] Email notifications
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Route optimization algorithms
- [ ] Multi-language support
- [ ] Dark mode

## License

This project is open-source and available for educational purposes.

## Support

For issues or questions, please contact the development team.
