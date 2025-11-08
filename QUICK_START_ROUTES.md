# 🚌 CampusShuttle Bus Route System - Quick Start Guide

## ✅ What's Been Created

### 4 Organized Bus Routes for Bangalore

1. **Route R01 - North Bangalore** 
   - 11 stops | Driver: Vijay Kumar | Fee: ₹1,800-2,800/month
   - Coverage: Yelahanka → Hebbal → Kalyan Nagar → SJB

2. **Route R02 - East Bangalore**
   - 11 stops | Driver: Anjali Singh | Fee: ₹1,900-3,200/month
   - Coverage: Whitefield → Marathahalli → Indiranagar → SJB

3. **Route R03 - South Bangalore**
   - 11 stops | Driver: Unassigned | Fee: ₹1,600-2,700/month
   - Coverage: Banashankari → BTM → Jayanagar → SJB

4. **Route R04 - West Bangalore**
   - 11 stops | Driver: Unassigned | Fee: ₹1,500-2,600/month
   - Coverage: Yeshwanthpur → Malleshwaram → Rajajinagar → SJB

**All routes end at: SJB Institute of Technology** ✨

---

## 🎯 Features

### For Students
- ✅ Browse 4 routes with 44 total stops
- ✅ Register for a route online
- ✅ Select boarding stop from route
- ✅ Fee automatically calculated based on stop
- ✅ View registration status
- ✅ Dashboard shows route info

### For Drivers
- ✅ View assigned route (EMP101 has R01, EMP102 has R02)
- ✅ See registered students
- ✅ Access schedule

### For Admins
- ✅ Manage all routes and stops
- ✅ Approve student registrations
- ✅ Assign drivers to routes
- ✅ Track payments

---

## 🚀 Quick Start

### 1. Start Server
```bash
cd /Users/apple/Desktop/Workspace/Transport_Management_System
source venv/bin/activate
python manage.py runserver
```

### 2. Test As Student
1. Login: http://localhost:8000/login/
   - USN: `CS001`, Password: `student123`
2. Click "Routes" in sidebar
3. Browse routes and click "View Details"
4. Click "Register for Route"
5. Select route → Select your stop → See fee → Submit

### 3. View Registration
- Dashboard shows registration summary
- "My Registration" shows full details
- Fee displayed based on selected stop

### 4. Admin Access
- URL: http://localhost:8000/admin/
- Username: `admin`, Password: `admin123`
- Manage routes, approve registrations, assign drivers

---

## 💰 Fee Structure

| Distance Range | Monthly Fee |
|---------------|-------------|
| 2-5 km | ₹1,500 - 2,000 |
| 5-10 km | ₹2,000 - 2,500 |
| 10-15 km | ₹2,500 - 3,000 |
| 15+ km | ₹3,000 - 3,200 |

**Fees are based on distance from SJB Institute**

---

## 📋 Database Models Created

1. **BusRoute** - Route info, driver, schedule, capacity
2. **BusStop** - Stop details, timing, fare, location
3. **RouteRegistration** - Student registrations, payment status
4. **Attendance** - Daily attendance tracking

---

## 📊 Current Stats

- Routes: 4 (all active)
- Total Stops: 44 (11 per route)
- Total Capacity: 165 students
- Drivers Assigned: 2
- Students: 2 (ready to register!)

---

## 🎨 User Journey

### Student Registration Flow:
1. Login → Dashboard
2. Click "Routes" → Browse all routes
3. Click route → See all stops with fares
4. "Register for Route" → Select route & stop
5. Fee auto-calculates → Submit
6. "My Registration" → View all details

### Dynamic Features:
- Stops load when route selected (AJAX)
- Fee updates when stop selected
- Seat availability shown
- Color-coded status badges

---

## 📝 Test Scenarios

### Scenario 1: Student Registration
```
1. Login as CS001 (student123)
2. Go to Routes
3. Click on "North Bangalore Route"
4. Click "Register for Route"
5. Select "R01 - North Bangalore"
6. Choose stop "Hebbal" (₹2,500/month)
7. See fee display, pickup time (7:22 AM)
8. Submit registration
9. Check "My Registration" page
```

### Scenario 2: Admin Approval
```
1. Login to admin panel (admin/admin123)
2. Go to Route Registrations
3. Find CS001's registration (Status: Pending)
4. Change status to "Active"
5. Set payment status to "Paid"
6. Save
```

### Scenario 3: Driver Assignment
```
1. Admin panel → Bus Routes
2. Click on Route R03 (South)
3. Select a driver from dropdown
4. Save
```

---

## 🔧 Management Commands

```bash
# Recreate all routes
python manage.py populate_routes

# Access Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser
```

---

## 📱 Pages Created

1. `/routes/` - List all routes
2. `/routes/<id>/` - Route details
3. `/routes/register/` - Registration form
4. `/routes/my-registration/` - Student's registration
5. `/api/route-stops/<id>/` - AJAX endpoint for stops

---

## 🎉 Success!

Your CampusShuttle now has a complete bus route management system with:
- **4 professional routes** covering Bangalore
- **44 strategically placed stops**
- **Distance-based fee structure**
- **Student self-registration**
- **Driver assignments**
- **Admin control panel**

**Ready to transport students safely! 🚌✨**

---

## 📞 Support

For detailed documentation, see: `BUS_ROUTES_DOCUMENTATION.md`
For test credentials, open: `test_credentials.html`
