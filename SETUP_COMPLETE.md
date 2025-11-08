# CampusShuttle - Setup Complete! 🚌

## ✅ What's Been Completed

### 1. **Role-Based Authentication System**
   - **Students** sign up with: USN, Name, Email, Phone, Gender, Password
   - **Drivers** sign up with: Employee Number, Name, Email, Phone, Gender, Password
   - **Admins** sign up with: Username, Email, Password

### 2. **Role-Specific Login Credentials**
   - Students login with: **USN + Password**
   - Drivers login with: **Employee Number + Password**
   - Admins login with: **Username + Password**

### 3. **New Signup Flow**
   - First, users select their role (Student/Driver/Admin)
   - Then, a role-specific form appears with appropriate fields
   - Clean, modern UI with role indicators and easy role switching

### 4. **Database & Models**
   - Custom User model with fields: `usn`, `emp_no`, `gender`, `role`, etc.
   - Migrations successfully applied
   - All necessary fields properly configured

### 5. **Test Accounts Created**
   - **2 Students**: CS001, CS002
   - **2 Drivers**: EMP101, EMP102
   - **1 Admin**: admin

---

## 🎯 How to Use

### Access the System
1. **Start Server** (if not running):
   ```bash
   cd /Users/apple/Desktop/Workspace/Transport_Management_System
   source venv/bin/activate
   python manage.py runserver
   ```

2. **View Test Credentials**:
   - Open: `/Users/apple/Desktop/Workspace/Transport_Management_System/test_credentials.html` in browser
   - Click copy buttons to easily copy credentials

3. **Navigate to**:
   - Landing Page: http://localhost:8000/
   - Login: http://localhost:8000/login/
   - Signup: http://localhost:8000/signup/

---

## 👥 Test Accounts

### Students (Login with USN)
| Name | USN | Password | Email |
|------|-----|----------|-------|
| Rahul Sharma | CS001 | student123 | rahul.sharma@campusshuttle.edu |
| Priya Patel | CS002 | student123 | priya.patel@campusshuttle.edu |

### Drivers (Login with Employee Number)
| Name | Emp No | Password | Email |
|------|--------|----------|-------|
| Vijay Kumar | EMP101 | driver123 | vijay.kumar@campusshuttle.edu |
| Anjali Singh | EMP102 | driver123 | anjali.singh@campusshuttle.edu |

### Admin (Login with Username)
| Name | Username | Password | Email |
|------|----------|----------|-------|
| System Administrator | admin | admin123 | admin@campusshuttle.edu |

---

## 📁 Project Structure

```
Transport_Management_System/
├── core/
│   ├── models.py          # Custom User model with role-specific fields
│   ├── forms.py           # StudentSignUpForm, DriverSignUpForm, AdminSignUpForm
│   ├── views.py           # Role-based signup and login views
│   ├── templates/core/
│   │   ├── landing.html      # CampusShuttle landing page
│   │   ├── signup.html       # Role selection + role-specific forms
│   │   ├── login.html        # Unified login page
│   │   ├── dashboard_admin.html
│   │   ├── dashboard_driver.html
│   │   └── dashboard_student.html
│   └── static/core/
│       ├── css/
│       │   ├── style.css
│       │   ├── auth.css
│       │   └── dashboard.css
│       └── js/
│           └── main.js
├── create_users.py        # Script to create dummy accounts
├── test_credentials.html  # Beautiful credentials reference page
└── db.sqlite3            # Database with all test accounts
```

---

## 🎨 Features

### Signup Process
1. **Role Selection Screen**: Choose Student, Driver, or Admin
2. **Dynamic Form**: Form fields change based on selected role
3. **Role Indicator**: Shows current role with option to change
4. **Validation**: Each form validates role-specific requirements

### Login System
- Unified login field accepts USN, Employee Number, or Username
- Backend authenticates based on the credential type
- Redirects to role-specific dashboard after login

### Dashboards
- **Student Dashboard**: View routes, book rides, track shuttle
- **Driver Dashboard**: View assigned routes, mark attendance, update status
- **Admin Dashboard**: Manage users, routes, buses, generate reports

---

## 🔒 Security Features
- Password hashing with Django's built-in system
- CSRF protection on all forms
- Role-based access control
- Unique constraints on USN and Employee Numbers

---

## 🚀 Next Steps (Optional Enhancements)
- [ ] Add password reset functionality
- [ ] Implement email verification
- [ ] Add profile picture upload
- [ ] Create route management system
- [ ] Build bus tracking feature
- [ ] Add booking system for students
- [ ] Implement real-time notifications

---

## 📝 Notes
- All passwords for test accounts are simple (student123, driver123, admin123)
- Admin account has superuser privileges
- Database is SQLite (for production, consider PostgreSQL)
- Static files are properly configured and serving

---

**Enjoy your CampusShuttle system! 🎓🚌**
