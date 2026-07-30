from flask import Flask, request
from auto_healing import auto_heal

app = Flask(__name__)


@app.route("/")
def home():
    return "Sentinel AI Engine is Running 🚀"


@app.route("/alert", methods=["POST"])
def receive_alert():
    data = request.json

    if not data:
        return {"status": "No data received"}, 400

    alerts = data.get("alerts", [])

    for alert in alerts:
        alert_name = alert.get("labels", {}).get("alertname", "Unknown")
        severity = alert.get("labels", {}).get("severity", "Unknown")

        print("\n" + "=" * 50)
        print("🚨 AI ALERT RECEIVED")
        print("=" * 50)
        print(f"Alert Name : {alert_name}")
        print(f"Severity   : {severity}")

        if alert_name == "HighCPUUsage":
            print("🤖 AI Decision: CPU usage is high.")
            print("➡ Recommendation: Investigate or restart the affected service.")

        elif alert_name == "HighMemoryUsage":
            print("🤖 AI Decision: Memory usage is high.")
            print("➡ Recommendation: Investigate memory usage.")

        elif alert_name == "NodeDown":
            print("🤖 AI Decision: Node Exporter is down.")
            print("🔄 Starting Auto-Healing...")
            auto_heal()

        else:
            print("🤖 AI Decision: No action required.")

        print("=" * 50)

    return {"status": "Alert processed successfully"}, 200


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Sentinel AI Engine Started Successfully")
    print("Listening on: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(host="0.0.0.0", port=5000, debug=True)