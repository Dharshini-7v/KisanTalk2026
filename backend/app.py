"""
KisanTalk - Voice-Based Farmers Grievance Redressal System
IVR Backend using Flask + SQLite + Whisper STT
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
import sqlite3
import os
import json
import uuid
from pathlib import Path
import subprocess
import tempfile

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
DATABASE_FOLDER = 'database'
GRIEVANCE_DB = os.path.join(DATABASE_FOLDER, 'grievances.db')

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATABASE_FOLDER, exist_ok=True)

# ======================== DATABASE SETUP ========================

def init_db():
    """Initialize SQLite database with grievance table"""
    conn = sqlite3.connect(GRIEVANCE_DB)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grievances (
            id TEXT PRIMARY KEY,
            phone_number TEXT NOT NULL,
            language TEXT NOT NULL,
            transcript TEXT,
            audio_file TEXT,
            category TEXT,
            department TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# ======================== UTILITY FUNCTIONS ========================

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(GRIEVANCE_DB)
    conn.row_factory = sqlite3.Row
    return conn

def generate_complaint_id():
    """Generate unique complaint ID like GRV-20260204-ABC123"""
    timestamp = datetime.now().strftime("%Y%m%d")
    random_id = str(uuid.uuid4())[:6].upper()
    return f"GRV-{timestamp}-{random_id}"

def classify_grievance(text):
    """
    Simple keyword-based classification
    Returns: (category, department, confidence)
    """
    text_lower = text.lower()
    
    # Define keywords for each category
    categories = {
        'Crop Issues': {
            'keywords': ['crop', 'disease', 'pest', 'plant', 'wilting', 'yellowing', 'fungal', 'blight', 'rust'],
            'department': 'Agricultural Department'
        },
        'Irrigation': {
            'keywords': ['water', 'irrigation', 'canal', 'well', 'pump', 'flooding', 'drought', 'dam'],
            'department': 'Water Resources Department'
        },
        'Crop Insurance': {
            'keywords': ['insurance', 'coverage', 'claim', 'premium', 'scheme', 'compensation', 'loss'],
            'department': 'Insurance & Finance Department'
        },
        'Fertilizer / Seeds': {
            'keywords': ['fertilizer', 'seed', 'manure', 'compost', 'nitrogen', 'quality', 'supplied'],
            'department': 'Agri-Input Supply Department'
        },
        'Market Access': {
            'keywords': ['market', 'price', 'selling', 'buyer', 'fair', 'middle-man', 'procurement', 'rate'],
            'department': 'Market & Commerce Department'
        }
    }
    
    # Count keyword matches
    scores = {}
    for category, data in categories.items():
        count = sum(1 for keyword in data['keywords'] if keyword in text_lower)
        scores[category] = count
    
    # Find best match
    if max(scores.values()) > 0:
        best_category = max(scores, key=scores.get)
        confidence = scores[best_category] / len(text.split())
        return best_category, categories[best_category]['department'], confidence
    else:
        # Default category if no match found
        return 'General', 'General Grievance Department', 0.0

def transcribe_audio(audio_file_path):
    """
    Transcribe audio using Whisper
    Falls back to mock transcription if Whisper not available
    """
    try:
        # Try using Whisper via command line
        result = subprocess.run(
            ['whisper', audio_file_path, '--output_format=txt', '--output_dir=.', '--fp16=False', '--language=hi'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Read the generated .txt file
        txt_file = audio_file_path.replace('.wav', '.txt')
        if os.path.exists(txt_file):
            with open(txt_file, 'r', encoding='utf-8') as f:
                transcript = f.read().strip()
            os.remove(txt_file)  # Clean up
            return transcript
    except Exception as e:
        print(f"Whisper error: {e}")
    
    # Fallback: Mock transcription
    return "[DEMO TRANSCRIPT] This is a sample grievance about crop disease and irrigation issues."

# ======================== API ENDPOINTS ========================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'service': 'KisanTalk IVR Backend',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/ivr/language-selection', methods=['POST'])
def language_selection():
    """
    Step 1: Farmer selects language via DTMF keypad
    Input: phone_number, selected_digit (1-5)
    Output: language_code, prompt_message
    """
    data = request.json
    phone = data.get('phone_number', 'DEMO')
    digit = data.get('digit')
    
    language_map = {
        '1': {'code': 'hi', 'name': 'हिंदी (Hindi)', 'prompt': 'कृपया अपनी समस्या बताएं।'},
        '2': {'code': 'ta', 'name': 'தமிழ் (Tamil)', 'prompt': 'தயவுசெய்து உங்கள் பிரச்சினையைக் கூறுங்கள்.'},
        '3': {'code': 'en', 'name': 'English', 'prompt': 'Please describe your grievance.'},
        '4': {'code': 'gu', 'name': 'ગુજરાતી (Gujarati)', 'prompt': 'કૃપયા તમારી ફરિયાદ વર્ણવો.'},
        '5': {'code': 'pa', 'name': 'ਪੰਜਾਬੀ (Punjabi)', 'prompt': 'ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਸ਼ਿਕਾਇਤ ਦੱਸੋ।'}
    }
    
    if digit in language_map:
        lang = language_map[digit]
        return jsonify({
            'success': True,
            'language': lang['name'],
            'language_code': lang['code'],
            'prompt': lang['prompt'],
            'next_step': 'Record grievance'
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Invalid digit. Please select 1-5.'
        }), 400

@app.route('/api/ivr/record-grievance', methods=['POST'])
def record_grievance():
    """
    Step 2: Receive recorded audio file
    Input: phone_number, language_code, audio_file
    Output: grievance_id, status
    """
    phone = request.form.get('phone_number', 'DEMO')
    language = request.form.get('language', 'en')
    
    # Handle audio file
    if 'audio' in request.files:
        file = request.files['audio']
        filename = f"{uuid.uuid4()}.wav"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
    else:
        # Demo mode - create placeholder
        filename = f"{uuid.uuid4()}.wav"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, 'wb') as f:
            f.write(b'RIFF\x00\x00\x00\x00WAVEfmt ')  # Dummy WAV header
        
    # Generate complaint ID
    complaint_id = generate_complaint_id()
    
    # Transcribe audio
    transcript = transcribe_audio(filepath)
    
    # Classify grievance
    category, department, confidence = classify_grievance(transcript)
    
    # Store in database
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO grievances 
        (id, phone_number, language, transcript, audio_file, category, department, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (complaint_id, phone, language, transcript, filename, category, department, 'Pending'))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'complaint_id': complaint_id,
        'message': f'Grievance recorded successfully. Your complaint ID is {complaint_id}',
        'transcript': transcript,
        'category': category,
        'department': department,
        'confidence': round(confidence * 100, 1)
    })

@app.route('/api/grievances', methods=['GET'])
def get_grievances():
    """Get all grievances with optional filtering"""
    category_filter = request.args.get('category')
    search_id = request.args.get('search_id')
    
    conn = get_db()
    cursor = conn.cursor()
    
    query = 'SELECT * FROM grievances ORDER BY created_at DESC'
    params = []
    
    if category_filter:
        query = query.replace('ORDER', f"WHERE category = ? ORDER")
        params.append(category_filter)
    
    if search_id:
        if params:
            query = query.replace('WHERE', f"WHERE id LIKE ? AND")
        else:
            query = query.replace('ORDER', f"WHERE id LIKE ? ORDER")
        params.append(f"%{search_id}%")
    
    cursor.execute(query, params)
    grievances = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify({
        'success': True,
        'count': len(grievances),
        'grievances': grievances
    })

@app.route('/api/grievances/<grievance_id>', methods=['GET'])
def get_grievance(grievance_id):
    """Get specific grievance details"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grievances WHERE id = ?', (grievance_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'success': True,
            'grievance': dict(row)
        })
    else:
        return jsonify({'success': False, 'error': 'Grievance not found'}), 404

@app.route('/api/grievances/<grievance_id>/update-status', methods=['POST'])
def update_status(grievance_id):
    """Update grievance status (admin function)"""
    data = request.json
    new_status = data.get('status')
    
    if new_status not in ['Pending', 'In Progress', 'Resolved']:
        return jsonify({'success': False, 'error': 'Invalid status'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE grievances SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
        (new_status, grievance_id)
    )
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'message': f'Status updated to {new_status}'
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Dashboard statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM grievances')
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM grievances WHERE status = 'Pending'")
    pending = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM grievances WHERE status = 'Resolved'")
    resolved = cursor.fetchone()[0]
    
    cursor.execute('SELECT category, COUNT(*) as count FROM grievances GROUP BY category')
    category_stats = {row[0]: row[1] for row in cursor.fetchall()}
    
    conn.close()
    
    return jsonify({
        'total_grievances': total,
        'pending': pending,
        'resolved': resolved,
        'by_category': category_stats
    })

# ======================== DEMO DATA ========================

@app.route('/api/demo/create-sample', methods=['POST'])
def create_sample_grievance():
    """Create a sample grievance for demo purposes"""
    samples = [
        {
            'phone': '9876543210',
            'language': 'hi',
            'transcript': 'मेरी फसल में एक रोग है। पत्तियां पीली पड़ रही हैं और पौधे मर रहे हैं। कृपया मदद करें।',
            'category': 'Crop Issues'
        },
        {
            'phone': '9876543211',
            'language': 'ta',
            'transcript': 'என் வயலில் நீர் இல்லை. பம்பு சேதமடைந்துவிட்டது. கால்வாய் குளு குலாக உள்ளது.',
            'category': 'Irrigation'
        },
        {
            'phone': '9876543212',
            'language': 'en',
            'transcript': 'The seeds supplied to me are of poor quality. Many plants did not germinate. I demand compensation.',
            'category': 'Fertilizer / Seeds'
        }
    ]
    
    import random
    sample = random.choice(samples)
    
    complaint_id = generate_complaint_id()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO grievances 
        (id, phone_number, language, transcript, category, department, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        complaint_id,
        sample['phone'],
        sample['language'],
        sample['transcript'],
        sample['category'],
        'Sample Department',
        'Pending'
    ))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'complaint_id': complaint_id,
        'message': 'Sample grievance created',
        'sample': sample
    })

# ======================== MAIN ========================

if __name__ == '__main__':
    print("🌾 KisanTalk IVR Backend Starting...")
    print("📍 Running on http://localhost:5000")
    print("📊 Database: database/grievances.db")
    app.run(debug=True, host='0.0.0.0', port=5000)
