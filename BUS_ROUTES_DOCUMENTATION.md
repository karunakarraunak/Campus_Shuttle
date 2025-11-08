# CampusShuttle - Bus Route System Documentation 🚌

## ✅ System Overview

CampusShuttle now features a complete bus route management system with 4 organized routes covering all major areas of Bangalore, with SJB Institute of Technology as the central hub.

---

## 🗺️ Bus Routes

### Route 1: North Bangalore (R01)
- **Bus Number**: KA-01-AB-1234
- **Driver**: Vijay Kumar (EMP101)
- **Capacity**: 45 students
- **Departure Time**: 7:30 AM
- **Arrival at SJB**: 9:00 AM
- **Total Stops**: 11
- **Coverage**: Yelahanka, Hebbal, HBR Layout, Kalyan Nagar, Banaswadi

**Stops with Fares:**
1. Yelahanka New Town - ₹2,800/month (18.5 km)
2. Yelahanka Old Town - ₹2,700/month (17.2 km)
3. Jakkur Aerodrome - ₹2,600/month (15.8 km)
4. Hebbal - ₹2,500/month (14.2 km)
5. Manyata Tech Park - ₹2,400/month (13.5 km)
6. HBR Layout - ₹2,300/month (12.0 km)
7. Kalyan Nagar - ₹2,200/month (10.5 km)
8. HRBR Layout - ₹2,100/month (9.2 km)
9. Banaswadi - ₹2,000/month (8.0 km)
10. Kacharakanahalli - ₹1,800/month (6.5 km)
11. SJB Institute of Technology - Destination

---

### Route 2: East Bangalore (R02)
- **Bus Number**: KA-01-CD-5678
- **Driver**: Anjali Singh (EMP102)
- **Capacity**: 40 students
- **Departure Time**: 7:45 AM
- **Arrival at SJB**: 9:15 AM
- **Total Stops**: 11
- **Coverage**: Whitefield, ITPL, Marathahalli, Indiranagar, HAL

**Stops with Fares:**
1. Whitefield - ₹3,200/month (22.0 km)
2. ITPL Main Gate - ₹3,100/month (20.5 km)
3. Marathahalli Bridge - ₹2,900/month (18.0 km)
4. Kundalahalli - ₹2,800/month (16.5 km)
5. Brookefield - ₹2,700/month (15.0 km)
6. HAL Airport - ₹2,600/month (13.2 km)
7. Indiranagar - ₹2,400/month (11.5 km)
8. Domlur - ₹2,300/month (10.0 km)
9. Old Airport Road - ₹2,100/month (8.5 km)
10. Binnamangala - ₹1,900/month (6.0 km)
11. SJB Institute of Technology - Destination

---

### Route 3: South Bangalore (R03)
- **Bus Number**: KA-01-EF-9012
- **Driver**: Not Assigned (Available)
- **Capacity**: 42 students
- **Departure Time**: 7:15 AM
- **Arrival at SJB**: 8:45 AM
- **Total Stops**: 11
- **Coverage**: Banashankari, JP Nagar, BTM, Jayanagar, Majestic

**Stops with Fares:**
1. Banashankari - ₹2,700/month (16.5 km)
2. JP Nagar 7th Phase - ₹2,600/month (15.0 km)
3. BTM Layout - ₹2,500/month (13.5 km)
4. Jayanagar 4th Block - ₹2,400/month (12.0 km)
5. Lalbagh Main Gate - ₹2,300/month (10.5 km)
6. National College - ₹2,200/month (9.0 km)
7. Basavanagudi - ₹2,100/month (8.0 km)
8. Majestic - ₹2,000/month (6.5 km)
9. Shivajinagar - ₹1,800/month (4.5 km)
10. Richmond Circle - ₹1,600/month (3.0 km)
11. SJB Institute of Technology - Destination

---

### Route 4: West Bangalore (R04)
- **Bus Number**: KA-01-GH-3456
- **Driver**: Not Assigned (Available)
- **Capacity**: 38 students
- **Departure Time**: 7:30 AM
- **Arrival at SJB**: 8:50 AM
- **Total Stops**: 11
- **Coverage**: Yeshwanthpur, Peenya, Malleshwaram, Rajajinagar

**Stops with Fares:**
1. Yeshwanthpur - ₹2,600/month (14.0 km)
2. Sandal Soap Factory - ₹2,500/month (12.8 km)
3. Peenya Industrial Area - ₹2,400/month (11.5 km)
4. Jalahalli - ₹2,300/month (10.0 km)
5. Mathikere - ₹2,200/month (8.8 km)
6. Malleshwaram - ₹2,100/month (7.5 km)
7. Rajajinagar - ₹2,000/month (6.2 km)
8. Mahalaxmi Layout - ₹1,900/month (5.0 km)
9. Nagarbhavi - ₹1,700/month (3.5 km)
10. Rajarajeshwari Nagar - ₹1,500/month (2.0 km)
11. SJB Institute of Technology - Destination

---

## 💰 Fee Structure

### Pricing Model
- **Distance-based pricing**: Farther stops have higher monthly fees
- **Range**: ₹1,500 to ₹3,200 per month
- **Payment Frequency**: Monthly
- **Fee includes**: Daily morning pickup and drop to SJB Institute

### Fee Calculation
Fees are automatically calculated based on:
- Distance from SJB Institute of Technology
- Operational costs (fuel, maintenance, driver salary)
- Route popularity and demand

---

## 📝 How Students Register for Routes

### Step-by-Step Registration Process

1. **Login to CampusShuttle**
   - Use your USN and password
   - Example: USN: `CS001`, Password: `student123`

2. **View Available Routes**
   - Click "Routes" in the sidebar
   - Browse all 4 active routes
   - View route details (stops, timings, fares, available seats)

3. **Register for a Route**
   - Click "Register for Route"
   - Select your preferred route (R01, R02, R03, or R04)
   - Choose your nearest boarding stop
   - See the monthly fee automatically calculated
   - Add any special requirements (optional)
   - Submit registration

4. **Registration Status**
   - Status starts as "Pending" for admin approval
   - Admin can approve and activate the registration
   - Payment status tracked separately (Paid/Unpaid/Partial)

5. **View Registration**
   - Go to "My Registration" to see all details
   - View route info, stop info, fees, and payment status
   - Can cancel registration if needed

---

## 👨‍✈️ How Drivers are Assigned

### Driver Assignment Process

1. **Admin assigns drivers** to routes through:
   - Django Admin Panel
   - Or using management scripts

2. **Current Assignments**:
   - **Vijay Kumar (EMP101)** → Route R01 (North)
   - **Anjali Singh (EMP102)** → Route R02 (East)
   - Route R03 (South) → Unassigned
   - Route R04 (West) → Unassigned

3. **To Assign More Drivers**:
   ```bash
   cd /Users/apple/Desktop/Workspace/Transport_Management_System
   source venv/bin/activate
   python manage.py shell
   ```
   
   Then in Python shell:
   ```python
   from core.models import User, BusRoute
   
   # Get a driver
   driver = User.objects.get(emp_no='EMP103')
   
   # Get a route
   route = BusRoute.objects.get(route_number='R03')
   
   # Assign
   route.driver = driver
   route.save()
   ```

---

## 🎯 Features Implemented

### For Students
- ✅ Browse all available routes with full details
- ✅ View stops, timings, and fees for each route
- ✅ Register for a route and select boarding stop
- ✅ View registration details and status
- ✅ See monthly fee based on selected stop
- ✅ Cancel registration
- ✅ Dashboard shows registration summary

### For Drivers
- ✅ View assigned routes
- ✅ See list of registered students
- ✅ Access route details and schedule

### For Admins
- ✅ Manage all routes, stops, and registrations
- ✅ Approve/reject student registrations
- ✅ Assign drivers to routes
- ✅ Update payment status
- ✅ View system statistics
- ✅ Add/edit/delete routes and stops

---

## 🗄️ Database Models

### BusRoute
- Route information (name, number, description)
- Bus details (number, capacity)
- Driver assignment
- Schedule (departure/arrival times)
- Status (active/inactive/maintenance)

### BusStop
- Stop details (name, order, location)
- Distance from SJB
- Pickup time
- Monthly fare
- GPS coordinates (optional)

### RouteRegistration
- Student-route association
- Selected bus stop
- Registration status (pending/active/cancelled)
- Payment status (paid/unpaid/partial)
- Monthly fee
- Start/end dates
- Special requirements

### Attendance
- Daily attendance tracking
- Boarding status and time
- Marked by driver
- Notes field

---

## 📊 System Statistics

### Current Status
- **Total Routes**: 4
- **Total Stops**: 44 (11 per route)
- **Total Capacity**: 165 students (across all routes)
- **Assigned Drivers**: 2
- **Available Routes**: 4 (all active)

---

## 🚀 How to Use the System

### Start the Server
```bash
cd /Users/apple/Desktop/Workspace/Transport_Management_System
source venv/bin/activate
python manage.py runserver
```

### Access Points
- **Landing Page**: http://localhost:8000/
- **Login**: http://localhost:8000/login/
- **Routes List**: http://localhost:8000/routes/
- **Register Route**: http://localhost:8000/routes/register/
- **Admin Panel**: http://localhost:8000/admin/

### Test Accounts
**Students**:
- USN: `CS001`, Password: `student123` (Rahul Sharma)
- USN: `CS002`, Password: `student123` (Priya Patel)

**Drivers**:
- Emp No: `EMP101`, Password: `driver123` (Vijay Kumar - Route R01)
- Emp No: `EMP102`, Password: `driver123` (Anjali Singh - Route R02)

**Admin**:
- Username: `admin`, Password: `admin123`

---

## 🎨 User Interface

### Student Flow
1. Dashboard → Shows registration status
2. Routes → Browse all routes
3. Route Detail → View specific route info
4. Register Route → Dynamic form with stop selection
5. My Registration → View complete registration details

### Key Features
- **Dynamic Stop Loading**: Stops load based on selected route via AJAX
- **Real-time Fee Display**: Monthly fee updates when stop is selected
- **Responsive Design**: Works on all devices
- **Visual Indicators**: Color-coded status badges
- **Seat Availability**: Shows available seats per route

---

## 📝 Administrative Tasks

### Using Django Admin
1. Login to admin: http://localhost:8000/admin/
2. Use admin credentials: `admin` / `admin123`

### Common Tasks:

**Approve Student Registration**:
1. Go to "Route registrations"
2. Find pending registration
3. Change status to "Active"
4. Update payment status if needed
5. Save

**Add New Route**:
1. Go to "Bus routes"
2. Click "Add bus route"
3. Fill in details
4. Add stops inline
5. Save

**Modify Fees**:
1. Go to "Bus stops"
2. Find the stop
3. Update "Base fare"
4. Save

---

## 🔄 Management Commands

### Populate Routes
```bash
python manage.py populate_routes
```
Creates all 4 routes with stops and fares.

### Create Superuser
```bash
python manage.py createsuperuser
```

---

## 📱 Future Enhancements

Potential features to add:
- [ ] Real-time bus tracking with GPS
- [ ] Mobile app integration
- [ ] Push notifications for bus arrival
- [ ] Online payment gateway
- [ ] QR code-based boarding
- [ ] Route optimization
- [ ] Student feedback system
- [ ] Emergency SOS feature
- [ ] Bus occupancy tracking
- [ ] Analytics dashboard

---

## 🎉 Summary

Your CampusShuttle system now has:
✅ 4 fully functional bus routes covering Bangalore
✅ 44 strategically placed stops
✅ Distance-based fee structure (₹1,500 - ₹3,200/month)
✅ Student route registration system
✅ Driver assignment functionality
✅ Complete admin management panel
✅ Real-time seat availability tracking
✅ Payment status monitoring
✅ Professional, modern UI

All routes converge at **SJB Institute of Technology** as the central hub! 🚌
