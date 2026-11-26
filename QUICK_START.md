# 🚀 KisanTalk - Quick Start Guide

## ⏱️ Get Running in 5 Minutes

### Step 1: Open Command Prompt
```
Windows Key + R → type "cmd" → press Enter
```

### Step 2: Navigate to Project
```cmd
cd "C:\Users\Dharshini\Desktop\KisanTalk-2026"
```

### Step 3: Activate Python Environment
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies
```cmd
cd backend
pip install -r requirements.txt
```

### Step 5: Start Backend
```cmd
python app.py
```

You should see:
```
🌾 KisanTalk IVR Backend Starting...
📍 Running on http://localhost:5000
📊 Database: database/grievances.db
```

### Step 6: Open Dashboard
1. Open browser
2. Go to: `file://C:/Users/Dharshini/Desktop/KisanTalk-2026/frontend/index.html`

### Step 7: Test It!
1. Click "Create Demo Grievance"
2. View in "Grievances" tab
3. Click "View" to see details
4. Go to "IVR Simulator" tab to submit your own

---

## 📱 IVR Simulator Guide

### Using the Simulator:
1. **Select Language**: Press 1 (Hindi), 2 (Tamil), 3 (English), 4 (Gujarati), or 5 (Punjabi)
2. **Enter Grievance**: Type your grievance (or leave blank for sample)
3. **Submit**: Click "Submit Grievance"
4. **Get Complaint ID**: Copy your complaint ID for tracking

### Example Grievances:
- **Crop Issues**: "My crop has a disease, leaves are turning yellow"
- **Irrigation**: "No water in the canal, my well pump is broken"
- **Seeds**: "The seeds you gave me didn't germinate properly"
- **Market**: "The price offered for my crop is too low"
- **Insurance**: "My insurance claim was rejected without reason"

---

## 🎯 What You Can Do

### Admin Dashboard
- ✅ View all grievances
- ✅ Filter by category
- ✅ Search by complaint ID
- ✅ View full details
- ✅ Update status (Pending → In Progress → Resolved)
- ✅ See statistics

### IVR Simulator
- ✅ Simulate farmer calls
- ✅ Test language selection
- ✅ Submit grievances
- ✅ See auto-classification
- ✅ Get complaint ID

### Backend APIs (for developers)
- ✅ POST /api/ivr/language-selection
- ✅ POST /api/ivr/record-grievance
- ✅ GET /api/grievances
- ✅ GET /api/grievances/{id}
- ✅ POST /api/grievances/{id}/update-status
- ✅ GET /api/stats

---

## 🐛 Troubleshooting

### Port 5000 already in use?
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID> /F
python app.py
```

### Python not found?
Install from: https://www.python.org/downloads/
Make sure to check "Add Python to PATH"

### Can't open frontend/index.html?
Use this path instead:
```
C:\Users\Dharshini\Desktop\KisanTalk-2026\frontend\index.html
```

### Database errors?
Delete `backend/database/grievances.db` and restart - it will auto-create

### Whisper errors?
```cmd
pip install openai-whisper
whisper --model tiny
```

---

## 📊 Sample Data

The system comes with:
- ✅ 3 demo grievance templates
- ✅ 5 languages pre-configured
- ✅ 5 grievance categories
- ✅ SQLite database ready to use
- ✅ Auto-classification working

---

## 🎓 For Demonstration

### Quick Demo (5 min):
1. Start backend (Step 5 above)
2. Open dashboard
3. Click "Create Demo Grievance" (3 times)
4. Show statistics
5. Filter by category
6. Update status
7. Show IVR Simulator

### Full Demo (15 min):
1. Explain system architecture
2. Show backend running
3. Create grievances manually via IVR
4. Show auto-classification working
5. Show filtering and search
6. Explain multi-language support
7. Show API endpoints with cURL

### Developer Demo (30 min):
1. Show code structure
2. Explain keyword-based classification
3. Demo API endpoints
4. Show database schema
5. Explain Flask routing
6. Show frontend code
7. Discuss scalability

---

## 📋 Checklist Before Submission

- ✅ Backend starts without errors
- ✅ Frontend dashboard loads
- ✅ Demo grievances display
- ✅ IVR simulator works
- ✅ Classification working
- ✅ Multi-language support
- ✅ Status updates working
- ✅ All APIs responding
- ✅ README complete
- ✅ Code commented

---

## 🎉 You're Ready!

Your KisanTalk system is:
- ✅ Running locally
- ✅ Fully functional
- ✅ Demo-ready
- ✅ Well-documented
- ✅ Easy to explain

Good luck with your presentation! 🚀

---

**Last updated**: February 4, 2026
**Status**: Ready for Demo & Submission
