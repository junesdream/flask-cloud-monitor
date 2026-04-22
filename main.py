import logging
import requests
from flask import Flask, jsonify

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cloud-monitor")

app = Flask(__name__)

# registry of monitored services (name → health endpoint)
SERVICES = {
    "Nexus-Data-API": "http://127.0.0.1:8000/",
    "AI-Bridge-Service": "http://127.0.0.1:8001/"
}


# basic health check for the monitor itself
@app.route('/')
def index():
    """Root endpoint for System Health."""
    return jsonify({"system": "Cloud Monitor", "status": "active"})


 # check availability of all services via HTTP requests
@app.route('/status')
def status_check():
    """Checks the health of all registered services."""
    logger.info("Starting global health check...")
    results = {}

    # iterate over all registered services
    for name, url in SERVICES.items():
        try:

            # timeout prevents blocking if service is down
            response = requests.get(url, timeout=1)
            results[name] = "Online" if response.status_code == 200 else "Offline"
        # service unreachable → mark as offline
        except requests.exceptions.RequestException:
            results[name] = "Offline (No Connection)"

    return jsonify(results)


if __name__ == '__main__':
    app.run(port=5000)