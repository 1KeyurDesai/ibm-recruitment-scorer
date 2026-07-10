# ResuMatch AI (IBM Recruitment Scorer)

Hybrid-cloud **AI agent** for automated resume screening: match candidates to job descriptions, return a **fit score (0–100)** with shortlist/reject guidance and reasoning.

Built by **Team AIGINITE** for the **IBM Dev Day — AI Demystified** hackathon.

---

## What it does

1. Recruiter triggers scoring via **IBM watsonx Orchestrate**
2. Job description + resume text/PDF are sent to a Python scoring backend
3. Engine evaluates skill overlap, density, and experience relevance
4. Agent returns **fit score + justification** for transparent shortlisting

---

## Results (hackathon eval)

- **90%+** match precision on multi-skill JD alignment (project validation set)
- Near-instant screening vs manual first-pass review
- Explainable outputs for HR decision support

---

## Tech stack

| Component | Technology |
|-----------|------------|
| Orchestration | IBM watsonx Orchestrate |
| NLU / extraction | IBM watsonx.ai |
| Scoring API | Python · Flask |
| Dashboard | Streamlit |
| Tunnel (demo) | ngrok |
| Contract | `openapi.json` |

---

## Repo structure

```
app.py           # scoring API + core logic
frontend.py      # Streamlit analytics dashboard
openapi.json     # watsonx / IBM integration contract
resumes.json     # sample resumes
jobs.csv         # sample jobs
```

---

## Quick start

```bash
git clone https://github.com/1KeyurDesai/ibm-recruitment-scorer.git
cd ibm-recruitment-scorer
pip install -r requirements.txt   # if present; else: pip install flask streamlit

python app.py
# optional dashboard
streamlit run frontend.py
```

Connect to IBM:

```bash
ngrok http 5000
```

Import `openapi.json` into watsonx Orchestrate and point the agent at your tunnel URL.

---

## Team AIGINITE

Keyur · Nikole · Shruti · Drishty

---

## License

Add MIT (or hackathon-required license) via GitHub UI.
