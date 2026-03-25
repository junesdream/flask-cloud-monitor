import logging
import requests
from flask import Flask, jsonify

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cloud-monitor")

app = Flask(__name__)

SERVICES = {
    "Nexus-Data-API": "http://127.0.0.1:8000/",
    "AI-Bridge-Service": "http://127.0.0.1:8001/"
}


@app.route('/')
def index():
    """Root endpoint for System Health."""
    return jsonify({"system": "Cloud Monitor", "status": "active"})


@app.route('/status')
def status_check():
    """Checks the health of all registered services."""
    logger.info("Starting global health check...")
    results = {}

    for name, url in SERVICES.items():
        try:

            response = requests.get(url, timeout=1)
            results[name] = "Online" if response.status_code == 200 else "Offline"
        except:
            results[name] = "Offline (No Connection)"

    return jsonify(results)


if __name__ == '__main__':
    app.run(port=5000)