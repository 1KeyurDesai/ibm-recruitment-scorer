from flask import Flask, request, jsonify

app = Flask(__name__)

# --- 1. HEALTH CHECK (To confirm it works) ---
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Campus Recruitment Copilot is RUNNING", "ready": True})

# --- 2. THE SKILL (What IBM Orchestrate will call) ---
@app.route('/score_candidate', methods=['POST'])
def score_candidate():
    try:
        # Get data from IBM Orchestrate
        data = request.json
        resume_text = data.get('resume_text', '').lower()
        job_desc = data.get('job_desc', '').lower()
        
        # Simple Logic: Count matching keywords
        keywords = job_desc.split()
        if not keywords:
            return jsonify({"score": 0, "decision": "Error", "explanation": "No job description provided"})
            
        matches = sum(1 for word in keywords if word in resume_text)
        score = int((matches / len(keywords)) * 100)
        
        # Cap score at 100
        score = min(100, score)
        
        # Decision Logic
        decision = "Shortlist" if score > 50 else "Reject"
        explanation = f"Candidate matched {matches} out of {len(keywords)} keywords."

        return jsonify({
            "score": score,
            "decision": decision,
            "explanation": explanation
        })
    except Exception as e:
        return jsonify({"score": 0, "decision": "Error", "explanation": str(e)})

if __name__ == '__main__':
    # Run on port 5000
    app.run(host='0.0.0.0', port=5000)