# ResuMatch AI (IBM Recruitment Scorer) 🚀
**A Hybrid Cloud Agent for Automated Resume Screening**

*Built by Team AIGINITE for the IBM Dev Day AI Demystified Hackathon.*

## 📖 Project Overview
Recruiters are overwhelmed by volume. Manual screening leads to fatigue and bias. 
**ResuMatch AI** (formerly IBM Recruitment Scorer) is an agentic AI tool that integrates **IBM watsonx Orchestrate** with a custom Python scoring engine. It instantly parses resumes, matches them against job descriptions, and provides a 0-100 fit score with a "Shortlist/Reject" decision.

## 🛠️ Tech Stack
* **Orchestrator:** IBM watsonx Orchestrate (Primary Agent Interface)
* **Backend:** Python (Flask) for scoring algorithms
* **Frontend (Optional):** Streamlit (for Admin/Visual Dashboard)
* **Connectivity:** ngrok (Secure Tunneling)
* **Data:** Synthetic JSON/CSV datasets

## ⚙️ How It Works
1.  **Trigger:** The HR user asks the Agent to "Score a candidate" via the IBM Orchestrate chat.
2.  **Input:** The user provides the *Job Description* and *Resume Text*.
3.  **Process:** * IBM Orchestrate sends this data to our local Python backend via a secure `ngrok` tunnel.
    * The Python engine calculates keyword overlap, skill matching, and experience relevance.
4.  **Result:** The Agent returns a "Fit Score" (e.g., 77/100) and a recommendation.

## 📂 File Structure
* `app.py` - The core Python logic for scoring candidates.
* `frontend.py` - A modern Streamlit dashboard for visualizing scores.
* `openapi.json` - The API specification connecting IBM Cloud to our local backend.
* `resumes.json` - Sample synthetic candidate data.
* `jobs.csv` - Sample job descriptions.

## 🚀 How to Run Locally
1.  **Start the Backend:**
    ```bash
    python app.py
    ```
2.  **Start the Dashboard (Optional):**
    ```bash
    streamlit run frontend.py
    ```
3.  **Connect to IBM:**
    * Use `ngrok http 5000` to open the tunnel.
    * Import `openapi.json` into IBM watsonx Orchestrate.

---

### 👥 Team AIGINITE
* **Keyur**
* **Nikole**
* **Shruti**
* **Drishty**
