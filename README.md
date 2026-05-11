# ResuMatch AI (IBM Recruitment Scorer) 🚀
**A Hybrid Cloud Agent for Automated Resume Screening**

*Built by Team AIGINITE for the IBM Dev Day AI Demystified Hackathon.*

## 📖 Project Overview
Recruiters are often overwhelmed by high application volumes, leading to manual fatigue and unconscious bias. **ResuMatch AI** is an agentic AI tool designed to bridge the gap between enterprise cloud orchestration and custom ML scoring. By integrating **IBM watsonx Orchestrate** with a specialized Python engine, it automates the parsing and matching of resumes against job descriptions, providing objective, data-driven hiring recommendations.

## 📊 Key Performance Metrics
* **High Precision:** Achieved **90%+ match accuracy** in aligning candidate profiles with complex, multi-skill job descriptions.
* **Operational Efficiency:** Drastically reduced the initial screening bottleneck, enabling near-instantaneous candidate scoring and ranking.
* **Explainable AI (XAI):** Built with transparency in mind, providing defensible scoring justifications to assist HR teams in making informed decisions.

## 🛠️ Tech Stack
* **Orchestrator:** IBM watsonx Orchestrate (Primary Agent Interface)
* **AI Engine:** IBM watsonx.ai for natural language understanding and entity extraction
* **Backend:** Python (Flask) for custom NLP-based scoring algorithms
* **Dashboard:** Streamlit (Admin/Visual Analytics for recruitment tracking)
* **Connectivity:** ngrok (Secure Cloud-to-Local Tunneling)

## ⚙️ How It Works
1. **Trigger:** The recruiter initiates a "Score Candidate" request via the IBM Orchestrate chat interface.
2. **Input:** The system ingests the *Job Description* and *Resume Text* (or PDF) through the agentic interface.
3. **Process:** * IBM Orchestrate routes the data through a secure `ngrok` tunnel to the local Python backend.
    * The scoring engine evaluates **keyword overlap, skill density, and experience relevance**.
4. **Result:** The Agent delivers a **Fit Score (0-100)** alongside a "Shortlist/Reject" decision and a brief technical justification.

## 📂 File Structure
* `app.py` — Core Python logic containing the scoring algorithms and API endpoints.
* `frontend.py` — Streamlit dashboard for visualizing real-time recruitment analytics.
* `openapi.json` — API specification required for IBM Cloud/watsonx integration.
* `resumes.json` & `jobs.csv` — Synthetic datasets used for model validation and testing.

## 🚀 Getting Started

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
