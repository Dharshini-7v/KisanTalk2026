# 🧪 KisanTalk API Testing Guide

## Using Postman / cURL

### 1️⃣ Health Check
**Test if backend is running**

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "OK",
  "service": "KisanTalk IVR Backend",
  "timestamp": "2026-02-04T14:30:45.123456"
}
```

---

### 2️⃣ Create Demo Grievance
**Instant grievance creation for demo**

```bash
curl -X POST http://localhost:5000/api/demo/create-sample
```

Response:
```json
{
  "success": true,
  "complaint_id": "GRV-20260204-ABC123",
  "message": "Sample grievance created",
  "sample": {
    "phone": "9876543210",
    "language": "hi",
    "transcript": "मेरी फसल में रोग है...",
    "category": "Crop Issues"
  }
}
```

---

### 3️⃣ Get All Grievances
**List all submitted grievances**

```bash
curl http://localhost:5000/api/grievances
```

Response:
```json
{
  "success": true,
  "count": 5,
  "grievances": [
    {
      "id": "GRV-20260204-ABC123",
      "phone_number": "9876543210",
      "language": "hi",
      "transcript": "मेरी फसल में रोग है",
      "category": "Crop Issues",
      "department": "Agricultural Department",
      "status": "Pending",
      "created_at": "2026-02-04T14:30:45"
    },
    ...
  ]
}
```

---

### 4️⃣ Get Single Grievance
**View detailed information**

```bash
curl http://localhost:5000/api/grievances/GRV-20260204-ABC123
```

Response:
```json
{
  "success": true,
  "grievance": {
    "id": "GRV-20260204-ABC123",
    "phone_number": "9876543210",
    "language": "hi",
    "transcript": "मेरी फसल में रोग है...",
    "audio_file": "uuid-file.wav",
    "category": "Crop Issues",
    "department": "Agricultural Department",
    "status": "Pending",
    "created_at": "2026-02-04T14:30:45",
    "updated_at": "2026-02-04T14:30:45"
  }
}
```

---

### 5️⃣ Language Selection
**Simulate farmer pressing 1-5 on keypad**

```bash
curl -X POST http://localhost:5000/api/ivr/language-selection \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "9876543210",
    "digit": "1"
  }'
```

Language Options:
- `"1"` → Hindi (हिंदी)
- `"2"` → Tamil (தமிழ்)
- `"3"` → English
- `"4"` → Gujarati (ગુજરાતી)
- `"5"` → Punjabi (ਪੰਜਾਬੀ)

Response:
```json
{
  "success": true,
  "language": "हिंदी (Hindi)",
  "language_code": "hi",
  "prompt": "कृपया अपनी समस्या बताएं।",
  "next_step": "Record grievance"
}
```

---

### 6️⃣ Record Grievance (Text Mode)
**Submit grievance text (simulating STT)**

```bash
curl -X POST http://localhost:5000/api/ivr/record-grievance \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "phone_number=9876543210&language=hi&transcript=मेरी%20फसल%20में%20कीड़े%20हैं"
```

Response:
```json
{
  "success": true,
  "complaint_id": "GRV-20260204-XYZ789",
  "message": "Grievance recorded successfully. Your complaint ID is GRV-20260204-XYZ789",
  "transcript": "मेरी फसल में कीड़े हैं",
  "category": "Crop Issues",
  "department": "Agricultural Department",
  "confidence": 92.5
}
```

---

### 7️⃣ Update Grievance Status
**Admin updating the grievance status**

```bash
curl -X POST http://localhost:5000/api/grievances/GRV-20260204-ABC123/update-status \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'
```

Valid Status Values:
- `"Pending"` - Initial state
- `"In Progress"` - Being handled by department
- `"Resolved"` - Issue resolved

Response:
```json
{
  "success": true,
  "message": "Status updated to In Progress"
}
```

---

### 8️⃣ Get Dashboard Statistics
**View summary statistics**

```bash
curl http://localhost:5000/api/stats
```

Response:
```json
{
  "total_grievances": 15,
  "pending": 8,
  "resolved": 5,
  "by_category": {
    "Crop Issues": 5,
    "Irrigation": 3,
    "Crop Insurance": 2,
    "Fertilizer / Seeds": 3,
    "Market Access": 2
  }
}
```

---

## 🧪 Complete Test Workflow

### Test Scenario: Submit a Grievance

**Step 1: Select Language**
```bash
curl -X POST http://localhost:5000/api/ivr/language-selection \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "9876543210", "digit": "3"}'
```

**Step 2: Record Grievance**
```bash
curl -X POST http://localhost:5000/api/ivr/record-grievance \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "phone_number=9876543210&language=en&transcript=My%20crop%20has%20pests%20and%20needs%20help"
```

Save the `complaint_id` returned (e.g., `GRV-20260204-ABC123`)

**Step 3: View Grievance**
```bash
curl http://localhost:5000/api/grievances/GRV-20260204-ABC123
```

**Step 4: Update Status**
```bash
curl -X POST http://localhost:5000/api/grievances/GRV-20260204-ABC123/update-status \
  -H "Content-Type: application/json" \
  -d '{"status": "In Progress"}'
```

**Step 5: Verify Update**
```bash
curl http://localhost:5000/api/grievances/GRV-20260204-ABC123
```

---

## 🔍 Filtering & Search

### Get Grievances by Category
```bash
curl "http://localhost:5000/api/grievances?category=Crop%20Issues"
```

### Search by Complaint ID
```bash
curl "http://localhost:5000/api/grievances?search_id=GRV"
```

### Combined
```bash
curl "http://localhost:5000/api/grievances?category=Irrigation&search_id=ABC"
```

---

## 📊 Sample Test Data

### Create Multiple Samples
```bash
# Create first sample
curl -X POST http://localhost:5000/api/demo/create-sample
sleep 1

# Create second sample
curl -X POST http://localhost:5000/api/demo/create-sample
sleep 1

# Create third sample
curl -X POST http://localhost:5000/api/demo/create-sample

# View all
curl http://localhost:5000/api/grievances
```

---

## 🎯 Test Categories

### Crop Issues Keywords
- crop, disease, pest, plant, wilting, yellowing, fungal, blight

**Test:** "My crop has a fungal disease"
**Expected Category:** Crop Issues
**Expected Department:** Agricultural Department

### Irrigation Keywords
- water, irrigation, canal, well, pump, flooding, drought

**Test:** "No water in canal, pump is broken"
**Expected Category:** Irrigation
**Expected Department:** Water Resources Department

### Crop Insurance Keywords
- insurance, coverage, claim, premium, compensation, loss

**Test:** "My insurance claim was rejected"
**Expected Category:** Crop Insurance
**Expected Department:** Insurance & Finance Department

### Fertilizer/Seeds Keywords
- fertilizer, seed, manure, compost, nitrogen, quality

**Test:** "Seeds supplied are poor quality"
**Expected Category:** Fertilizer / Seeds
**Expected Department:** Agri-Input Supply Department

### Market Access Keywords
- market, price, selling, buyer, fair, procurement, rate

**Test:** "The market price is too low"
**Expected Category:** Market Access
**Expected Department:** Market & Commerce Department

---

## 🚀 Automation Script (Bash)

```bash
#!/bin/bash

# Test all endpoints
echo "1️⃣ Health Check"
curl http://localhost:5000/api/health | json_pp

echo -e "\n2️⃣ Create Sample"
RESPONSE=$(curl -s -X POST http://localhost:5000/api/demo/create-sample)
echo $RESPONSE | json_pp
COMPLAINT_ID=$(echo $RESPONSE | grep -o '"complaint_id":"[^"]*' | cut -d'"' -f4)

echo -e "\n3️⃣ Get All Grievances"
curl http://localhost:5000/api/grievances | json_pp

echo -e "\n4️⃣ Get Single Grievance: $COMPLAINT_ID"
curl http://localhost:5000/api/grievances/$COMPLAINT_ID | json_pp

echo -e "\n5️⃣ Update Status"
curl -X POST http://localhost:5000/api/grievances/$COMPLAINT_ID/update-status \
  -H "Content-Type: application/json" \
  -d '{"status": "In Progress"}' | json_pp

echo -e "\n6️⃣ Statistics"
curl http://localhost:5000/api/stats | json_pp
```

---

## 🔧 Troubleshooting API Tests

### Error: Connection refused
```
Backend not running. Start it first:
cd backend
python app.py
```

### Error: JSON decode error
```
Check Content-Type header is correct:
-H "Content-Type: application/json"
```

### Error: 404 Not Found
```
Check the endpoint URL is correct
Complaint ID format: GRV-YYYYMMDD-XXXXXX
```

### Error: CORS error (in browser)
```
CORS is already enabled in app.py
Check browser console for actual error
```

---

## 📈 Performance Notes

- Health check: < 10ms
- Create grievance: < 100ms
- Get list: < 50ms
- Get single: < 10ms
- Update status: < 10ms
- Stats: < 50ms

---

## ✅ Test Checklist

- [ ] Backend starts without errors
- [ ] Health endpoint responds
- [ ] Can create sample grievance
- [ ] Can list all grievances
- [ ] Can get single grievance
- [ ] Can update status
- [ ] Classification works correctly
- [ ] Complaint ID format correct (GRV-YYYYMMDD-XXXXXX)
- [ ] Timestamps are saved
- [ ] Statistics calculate correctly

---

**Last Updated:** February 4, 2026  
**Status:** Ready for Testing
