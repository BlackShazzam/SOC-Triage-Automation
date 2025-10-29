from flask import Flask, request, jsonify
import json, os, datetime, subprocess

app = Flask(__name__)

LOG_FILE = "/opt/splunk_project/artifacts/triagelogs.json"
ACTION_SCRIPT = "/opt/splunk_project/triage/action_log.sh"

def log_action(ip, hits):
    """Run the simple action script to record containment."""
    if ip:
        try:
            subprocess.Popen([ACTION_SCRIPT, ip, str(hits)])
        except Exception as e:
            print(f"⚠️ Action script failed for {ip}: {e}")

@app.route("/triage", methods=["POST"])
def receive_alert():
    data = request.get_json(force=True)
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "alert": data
    }

    # Extract IP + hits for the log_action
    alert_data = data.get("result") or data
    src_ip = alert_data.get("src_ip")
    hits = alert_data.get("hits", 0)

    # Save to triage log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    # Record containment action
    log_action(src_ip, hits)

    print(f"✅ Received alert: {data}")
    return jsonify({"status": "success", "received": data}), 200


@app.route("/health", methods=["GET"])
def health():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
