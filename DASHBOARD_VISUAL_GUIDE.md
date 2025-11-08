# 🎨 Dashboard Visual Guide - CampusShuttle

## Student Dashboard States

### State 1: Not Registered
```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Dashboard                                            │
│                                                         │
│ 📢 You're not registered for any bus route yet!        │
│                                                         │
│ 🚌 Browse Available Routes                             │
│    [Register Now →]  (Purple Gradient Button)          │
└─────────────────────────────────────────────────────────┘
```

### State 2: Pending Approval
```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Dashboard                                            │
│                                                         │
│ ⏳ Your Registration is Pending Admin Approval          │
│                                                         │
│ Route: Route 1 - North Bangalore                       │
│ Stop: Hebbal                                            │
│ Status: [Pending] (Yellow Badge)                       │
│                                                         │
│ [Cancel Registration] (Red Button)                     │
└─────────────────────────────────────────────────────────┘
```

### State 3: Active Registration
```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Dashboard                                            │
│                                                         │
│ ✅ Your Bus Schedule (Active)                          │
│                                                         │
│ 🚌 Route 1 - North Bangalore | Bus: KA01AB1234        │
│ 📍 Your Stop: Hebbal | ⏰ 7:30 AM                     │
│ 💰 Monthly Fare: ₹800                                  │
│                                                         │
│ [View Full Schedule] [Cancel Registration]             │
└─────────────────────────────────────────────────────────┘
```

---

## Driver Dashboard

### With Assigned Route
```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Driver Dashboard                                     │
│ Welcome back, Driver Name!                              │
│                                                         │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                  │
│ │ 🚌   │ │ 🎓   │ │ 📍   │ │ 💺   │                  │
│ │Route │ │ 25   │ │ 11   │ │ 15   │                  │
│ │ R1   │ │Stude-│ │Stops │ │ of   │                  │
│ │      │ │ nts  │ │      │ │ 40   │                  │
│ └──────┘ └──────┘ └──────┘ └──────┘                  │
│                                                         │
│ 📋 Route Information                                   │
│ ├─ Route Number: Route 1                              │
│ ├─ Route Name: North Bangalore                        │
│ ├─ Bus Number: KA01AB1234                             │
│ ├─ Departure: 7:00 AM                                 │
│ ├─ Arrival: 8:30 AM                                   │
│ └─ Capacity: 40 passengers                            │
│                                                         │
│ 📍 Bus Stops (11)                                      │
│ ① Hebbal      - 7:30 AM - 8.0 km - ₹800/mo           │
│ ② Mekhri      - 7:35 AM - 7.0 km - ₹700/mo           │
│ ...                                                     │
│                                                         │
│ 👥 Registered Students (25 Active)                    │
│ ┌────────────────────────────────────────────────────┐ │
│ │ USN    │ Name       │ Stop   │ Time    │ Status  │ │
│ │ SJB001 │ John Doe   │ Hebbal │ 7:30 AM │ Active  │ │
│ │ SJB002 │ Jane Smith │ Mekhri │ 7:35 AM │ Active  │ │
│ └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Without Assigned Route
```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Driver Dashboard                                     │
│                                                         │
│                        🚌                               │
│                                                         │
│              No Route Assigned                          │
│                                                         │
│    You haven't been assigned to any bus route yet.     │
│    Please contact the administrator to get assigned.   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Admin Dashboard

```
┌─────────────────────────────────────────────────────────┐
│ 🏠 Admin Dashboard                                      │
│ Welcome back, Admin Name!                               │
│                                                         │
│ ⚠️  Pending Approvals                                  │
│     You have 3 pending registrations waiting for        │
│     approval. [Review now →]                           │
│                                                         │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                  │
│ │ 🚌   │ │ 🎓   │ │ 👨‍✈️ │ │ ⏳   │                  │
│ │  4   │ │ 25   │ │  4   │ │  3   │                  │
│ │Route │ │Stude-│ │Drive-│ │Pendi-│                  │
│ │  s   │ │ nts  │ │ rs   │ │ ng   │                  │
│ └──────┘ └──────┘ └──────┘ └──────┘                  │
│                                                         │
│ 🚀 Quick Actions                                       │
│ ┌─────────────────────┬─────────────────────┐          │
│ │ ✅ Approve          │ 🚌 Manage           │          │
│ │    Registrations    │    Routes           │          │
│ │    Review pending   │    Add/edit routes  │          │
│ │    [→]             │    [→]              │          │
│ ├─────────────────────┼─────────────────────┤          │
│ │ 👨‍✈️ Assign         │ 👥 Manage           │          │
│ │    Drivers          │    Users            │          │
│ │    Assign to routes │    View all users   │          │
│ │    [→]             │    [→]              │          │
│ ├─────────────────────┼─────────────────────┤          │
│ │ 📍 Manage           │ ⚙️ Full             │          │
│ │    Bus Stops        │    Admin Panel      │          │
│ │    Add/modify stops │    Complete access  │          │
│ │    [→]             │    [→]              │          │
│ └─────────────────────┴─────────────────────┘          │
│                                                         │
│ 📊 System Summary                                      │
│ 🚌 Active Routes       - 4 routes operating            │
│ 🎓 Student Registrations - 25 active registrations     │
│ 👨‍✈️ Drivers            - 4 drivers in system          │
│ ⏳ Pending Approvals   - 3 registrations need review   │
│                                                         │
│ 📝 Admin Notes                                         │
│ Key Responsibilities:                                   │
│ ✅ Review and approve student registrations            │
│ ✅ Assign drivers to routes (one driver per route)     │
│ ✅ Monitor route capacity and availability             │
│ ✅ Manage bus routes and stops                         │
│ ✅ Handle system configuration                         │
│                                                         │
│ Business Rules:                                         │
│ 🔒 Only admins can approve registrations               │
│ 🔒 Students can register for only one route            │
│ 🔒 Each route can have only one driver                 │
│ 🔒 Route capacity is enforced automatically            │
└─────────────────────────────────────────────────────────┘
```

---

## Sidebar Navigation (All Dashboards)

### Student Dashboard
```
┌─────────────────┐
│ 🚌 CampusShuttle│
├─────────────────┤
│ 🏠 Dashboard    │ ← Active
│ 🚌 Browse Routes│
│ 📋 My Registr.  │
│ 👤 Edit Profile │
├─────────────────┤
│ 🚪 Logout       │
└─────────────────┘
```

### Driver Dashboard
```
┌─────────────────┐
│ 🚌 CampusShuttle│
├─────────────────┤
│ 🏠 Dashboard    │ ← Active
│ 👤 Edit Profile │
├─────────────────┤
│ 🚪 Logout       │
└─────────────────┘
```

### Admin Dashboard
```
┌─────────────────┐
│ 🚌 CampusShuttle│
├─────────────────┤
│ 🏠 Dashboard    │ ← Active
│ 👤 Edit Profile │
│ ⚙️ Admin Panel  │
├─────────────────┤
│ 🚪 Logout       │
└─────────────────┘
```

---

## Color Scheme

### Status Badges:
- **Active**: Green (#dcfce7 bg, #065f46 text)
- **Pending**: Yellow (#fef3c7 bg, #92400e text)
- **Inactive**: Red (#fee2e2 bg, #991b1b text)

### Stat Card Icons:
- **Routes (Blue)**: #dbeafe bg, #2563eb text
- **Students (Green)**: #dcfce7 bg, #16a34a text
- **Drivers (Yellow)**: #fef3c7 bg, #ca8a04 text
- **Pending (Red)**: #fee2e2 bg, #dc2626 text

### Buttons:
- **Primary**: Purple gradient (#667eea → #764ba2)
- **Success**: Green gradient (#10b981 → #059669)
- **Danger**: Red gradient (#ef4444 → #dc2626)

---

## Responsive Breakpoints

- **Mobile**: < 768px (Single column, stacked cards)
- **Tablet**: 768px - 1024px (2 columns)
- **Desktop**: > 1024px (Full grid layout)

---

## Interactive Elements

### Hover Effects:
- ✨ Cards lift 2px with shadow
- ✨ Buttons scale up 2%
- ✨ Links underline appears
- ✨ Table rows get background highlight
- ✨ Quick action cards get purple border

### Loading States:
- 🔄 Submit buttons show spinner
- 🔄 Registration form disables on submit
- 🔄 Cancel button confirms before action

### Animations:
- 🎯 Buttons bounce on hover
- 🎯 Shine effect sweeps across
- 🎯 Fade-in for page load
- 🎯 Slide-in for alerts

---

**Visual Consistency**: All dashboards share the same design language, color palette, and interaction patterns for a cohesive user experience! 🎨
