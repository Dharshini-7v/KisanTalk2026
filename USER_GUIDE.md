# 📱 KIISANTALK - VISUAL USER GUIDE

## 🏠 Dashboard Home Screen

When you open `frontend/index.html`, you'll see:

```
┌─────────────────────────────────────────────────────────┐
│          🌾 KisanTalk Admin Dashboard                   │
│  Voice-Based Farmers Grievance Redressal System         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [📊 Dashboard] [📋 Grievances] [☎️ IVR Simulator]    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    STATISTICS                           │
│  ┌──────────┬──────────┬──────────┐                    │
│  │    15    │    8     │    5     │                    │
│  │  Total   │ Pending  │ Resolved │                    │
│  └──────────┴──────────┴──────────┘                    │
│                                                         │
│  [➕ Create Demo Grievance] [🔄 Refresh Data]          │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Grievances Tab

See all submitted grievances:

```
┌─────────────────────────────────────────────────────────┐
│         FILTER & SEARCH                                │
│  [🔍 Search by ID....] [Category▼] [🔄 Refresh]      │
├─────────────────────────────────────────────────────────┤
│ Complaint ID      │ Phone    │ Category   │ Status     │
├─────────────────────────────────────────────────────────┤
│ GRV-20260204-ABC1 │ 9876543  │ Crop Issues│ Pending   │
│ GRV-20260204-ABC2 │ 9876543  │ Irrigation │ In Prog... │
│ GRV-20260204-ABC3 │ 9876543  │ Insurance  │ Resolved  │
│ ...               │ ...      │ ...        │ ...       │
└─────────────────────────────────────────────────────────┘

Click [View] to see details ↓

┌─────────────────────────────────────────────────────────┐
│          GRIEVANCE DETAILS                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ Complaint ID:  GRV-20260204-ABC123                     │
│ Phone:         9876543210                              │
│ Language:      HI                                       │
│                                                         │
│ Grievance:     मेरी फसल में कीटों का प्रकोप है       │
│                                                         │
│ Category:      [Crop Issues]                           │
│ Department:    Agricultural Department                │
│                                                         │
│ Status:        [Pending ▼]  ← Update here             │
│                                                         │
│ Created:       Feb 4, 2026 2:30 PM                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ☎️ IVR Simulator Tab

Test the complete IVR flow:

```
┌─────────────────────────────────────────────────────────┐
│          IVR SIMULATOR                                 │
│   Simulate a farmer calling the toll-free number       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  STEP 1: SELECT LANGUAGE                              │
│  ┌──────────┬──────────┬──────────┬──────────┐        │
│  │🇮🇳 हिंदी │🇮🇳 தமிழ் │🇬🇧 English│🇮🇳 ગુજ..│        │
│  │  (1)     │  (2)     │  (3)     │  (4)     │        │
│  └──────────┴──────────┴──────────┴──────────┘        │
│  Selected: हिंदी (Hindi)  ← Shows after selection    │
│                                                         │
│  STEP 2: RECORD GRIEVANCE                             │
│  ┌─────────────────────────────────────────────┐     │
│  │ Enter your grievance here (or use sample)...│     │
│  │                                             │     │
│  │ [✓] Use sample text if field is empty      │     │
│  └─────────────────────────────────────────────┘     │
│                                                         │
│  STEP 3: SUBMIT                                       │
│  Phone: [9876543210........] (optional)               │
│                                                         │
│  [✅ Submit Grievance]                                │
│                                                         │
│  RESULT (appears after submit):                       │
│  ┌─────────────────────────────────────────────┐     │
│  │ ✅ Grievance Submitted!                      │     │
│  │                                             │     │
│  │ Complaint ID: GRV-20260204-XYZ789           │     │
│  │ Language: Hindi                             │     │
│  │ Category: Crop Issues                       │     │
│  │ Department: Agricultural Department         │     │
│  │ Confidence: 92.5%                           │     │
│  │                                             │     │
│  │ 📱 Keep your Complaint ID for tracking!    │     │
│  └─────────────────────────────────────────────┘     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 How to Use: Step-by-Step

### Creating Your First Grievance (3 minutes)

```
STEP 1: Click "Create Demo Grievance"
        ↓
STEP 2: See success message with Complaint ID
        ↓
STEP 3: Go to "Grievances" tab
        ↓
STEP 4: See grievance in the table
        ↓
STEP 5: Click "View" to see details
        ↓
STEP 6: Update status and click save
        ↓
STEP 7: See status updated in table
```

### Creating Custom Grievance via IVR (4 minutes)

```
STEP 1: Go to "IVR Simulator" tab
        ↓
STEP 2: Click a language button (e.g., हिंदी)
        ↓
STEP 3: Type your grievance text (or leave blank)
        ↓
STEP 4: Enter phone number (optional)
        ↓
STEP 5: Click "Submit Grievance"
        ↓
STEP 6: See Complaint ID + Auto-Classification
        ↓
STEP 7: Go to Grievances tab to confirm
```

### Filtering & Searching (2 minutes)

```
STEP 1: Go to "Grievances" tab
        ↓
STEP 2: Select category from dropdown
        ↓
STEP 3: Results automatically filter
        ↓
STEP 4: Or type in search box for ID
        ↓
STEP 5: Results update in real-time
```

---

## 🎨 What You'll See

### Color Coding

**Status Badges:**
```
🟢 [Pending]      - Yellow/Orange background
🟡 [In Progress]  - Blue background
✅ [Resolved]     - Green background
```

**Category Badges:**
```
[Crop Issues]     - Light blue
[Irrigation]      - Light blue
[Insurance]       - Light blue
[Seeds]           - Light blue
[Market]          - Light blue
```

**Buttons:**
```
[Green] Create Demo, Submit Grievance
[Blue]  View, Refresh, Filter
[Red]   Delete (if implemented)
```

---

## 📊 Statistics You'll See

### Dashboard Stats
```
Total Grievances: 15
├── Pending: 8
├── In Progress: 3
└── Resolved: 5

By Category:
├── Crop Issues: 5
├── Irrigation: 3
├── Insurance: 2
├── Seeds: 3
└── Market: 2
```

### Auto-Calculated
- Total grievances count
- Pending grievances count
- Resolved grievances count
- Grievances per category
- Percentage calculations
- Status distribution

---

## 🔔 What Happens When You Submit

```
FARMER SUBMITS GRIEVANCE
         ↓
WHISPER TRANSCRIBES (or uses text)
         ↓
NLP CLASSIFIES AUTOMATICALLY
    (Analyzes keywords)
         ↓
DATABASE STORES
    (Saves to grievances.db)
         ↓
COMPLAINT ID GENERATES
    (GRV-YYYYMMDD-XXXXXX format)
         ↓
DASHBOARD UPDATES
    (Shows in grievances list)
         ↓
ADMIN NOTIFIED
    (Can update status)
         ↓
FARMER TRACKS
    (Using Complaint ID)
```

---

## 💾 Data Saved Per Grievance

When you submit a grievance, this is stored:

```
┌──────────────────────────────────┐
│ GRIEVANCE RECORD                 │
├──────────────────────────────────┤
│ Complaint ID:     GRV-YYYYMMDD-  │
│                   XXXXXX         │
│ Phone Number:     9876543210     │
│ Language:         hi/ta/en/gu/pa │
│ Transcript:       [Full text]    │
│ Audio File:       UUID.wav       │
│ Category:         [Auto-detected]│
│ Department:       [Assigned]     │
│ Status:           Pending/...    │
│ Created At:       [Timestamp]    │
│ Updated At:       [Timestamp]    │
└──────────────────────────────────┘
```

---

## 🗂️ Category Auto-Detection

When you submit, the system automatically determines:

```
INPUT: "मेरी फसल में कीटों का प्रकोप है"
       (My crop has pest infestation)
       
ANALYSIS:
├── Finds keyword "crop" ✓
├── Finds keyword "pest" ✓
└── Confidence: 85%+

OUTPUT:
├── Category: Crop Issues
├── Department: Agricultural Department
└── Confidence: 85%
```

**It uses keyword matching:**
```
Crop Issues keywords:    crop, disease, pest, wilting, fungal
Irrigation keywords:     water, canal, well, pump, flooding
Insurance keywords:      insurance, claim, compensation
Seeds keywords:          fertilizer, seed, quality
Market keywords:         market, price, buyer, procurement
```

---

## 🧪 Example Scenarios

### Scenario 1: Test Crop Issues
```
Language: English (Press 3)
Text: "My plants have a fungal disease"
Expected Output:
  ✓ Category: Crop Issues
  ✓ Department: Agricultural Department
  ✓ Confidence: 90%+
```

### Scenario 2: Test Irrigation
```
Language: Hindi (Press 1)
Text: "कोई पानी नहीं, कुआं सूख गया"
Expected Output:
  ✓ Category: Irrigation
  ✓ Department: Water Resources Department
  ✓ Confidence: 85%+
```

### Scenario 3: Test Market Access
```
Language: English (Press 3)
Text: "The market price is very low"
Expected Output:
  ✓ Category: Market Access
  ✓ Department: Market & Commerce Department
  ✓ Confidence: 80%+
```

---

## 🎯 Interactive Elements

### Buttons (Clickable)
```
[Button Name]        Function
────────────────────────────────────────
Create Demo          Instantly creates sample
Refresh              Reloads data from backend
Submit Grievance     Processes and stores
View                 Opens detail modal
Update Status        Changes grievance status
```

### Dropdowns (Selectable)
```
[Dropdown]           Options
────────────────────────────────────────
Language             Hindi, Tamil, English, Gujarati, Punjabi
Category Filter      All Categories, Crop Issues, Irrigation, etc.
Status Update        Pending, In Progress, Resolved
```

### Input Fields (Editable)
```
[Field]              Input Type
────────────────────────────────────────
Search Box           Text - searches complaint IDs
Grievance Text       Text - 200+ characters
Phone Number         Numeric - 10 digits
```

---

## ✅ Quick Test Checklist

Use this to verify everything works:

```
☐ Dashboard loads without errors
☐ Statistics display numbers
☐ "Create Demo Grievance" works
☐ Grievances table populates
☐ "View" button opens modal
☐ Detail modal shows all fields
☐ Status dropdown works
☐ Grievance list updates after status change
☐ Filter dropdown works
☐ Search box filters results
☐ IVR Simulator tab loads
☐ Language buttons respond
☐ Submit button processes grievance
☐ Complaint ID displays
☐ Category classification correct
```

---

## 🎓 For Demonstration

**Quick Demo Flow (5 min):**
```
1. Show dashboard
2. Click "Create Demo Grievance"
3. Show statistics update
4. Go to Grievances tab
5. Show grievance in table
6. Click "View"
7. Update status
8. Explain categorization
```

**Full Demo Flow (15 min):**
```
1. Show backend running
2. Open dashboard
3. Create multiple demos
4. Filter by category
5. Search by ID
6. Show IVR Simulator
7. Test language selection
8. Submit custom grievance
9. Show auto-classification
10. Explain architecture
```

---

## 🚀 Performance

What to expect:

```
Dashboard Load:        < 1 second
Create Grievance:      < 2 seconds
View Details:          Instant
Filter Results:        < 500ms
Search Results:        Real-time
Status Update:         < 1 second
Category Detection:    < 100ms
Database Query:        < 50ms
```

---

## 💡 Tips & Tricks

### For Better Demo:
1. Create 3-5 demo grievances first
2. Then show filtering in action
3. Make status updates dramatic
4. Test language switching
5. Show different grievance texts

### For Explanation:
1. Explain 5 categories clearly
2. Show keyword matching logic
3. Demonstrate complaint ID format
4. Explain database structure
5. Walk through API flow

---

**You're now ready to use KisanTalk!** 🎉

*For more details, see README.md or API_TESTING_GUIDE.md*
