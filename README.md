# SOC Triage Automation — Splunk + Python (Flask)

A compact SOC demo project where Splunk detects repeated SSH login failures and sends alerts to a Flask API that records and logs a simulated containment action.
It demonstrates how detection and response can be connected in a realistic SOC workflow.

---

## ⚙️ Workflow
- **Generate:** Simulated SSH login failures on a Linux VM  
- **Ingest:** Splunk Universal Forwarder forwards logs to Splunk Enterprise (port 9997)  
- **Parse:** Extracted `src_ip`, `status`, and `user` fields for analysis  
- **Alert:** Saved search `Detect_Failed_Sessions` triggers when IPs exceed failure threshold  
- **Triage:** Splunk alert sends webhook to Flask receiver (`reciever.py`)  
- **Action:** Flask logs alert data and runs `action_log.sh` to simulate a containment step  

---

## 🧩 Project Structure
SOC-Triage-Automation/
├── 1_log_generation/
│   └── log_sim.py
├── 2_splunk_setup/
│   ├── inputs.conf
│   ├── outputs.conf
│   └── field_extractions.txt
├── 3_triage/
│   ├── receiver.py
│   └── action_log.sh
├── example_outputs/
│   ├── triagelogs_sample.json
│   └── triage_actions_sample.log
├── screenshots/
└── README.md

---

## 🚀 Run Locally
cd 3_triage  
python3 reciever.py  

Then configure your Splunk alert webhook to send POST requests to:  
http://<YOUR_VM_IP>:8000/triage  

Example JSON payload:
{
  "search_name": "Detect_Failed_Sessions",
  "src_ip": "192.168.1.103",
  "hits": "6"
}

---

## 🛠️ Tools Used
- **Splunk Enterprise** — Log collection, search, and alerting  
- **Flask (Python)** — Lightweight webhook receiver  
- **Bash** — Simple action logger  
- **Linux (Parrot OS)** — Test environment  

---

## 📘 Notes
- All IPs, users, and alerts are simulated for demonstration only.  
- The “containment” step is a log entry, not a real network block.  
- Designed for SOC Analyst learning and portfolio demonstration.  

---

**Author:** Jay Kudtarkar
