# ☁️ Flask Cloud Monitor

Lightweight monitoring microservice for AI infrastructure.
Designed to track availability, latency, and operational health of distributed AI services in real time.

![CI Status](https://github.com/junesdream/flask-cloud-monitor/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🧠 Overview

Flask Cloud Monitor acts as a **central observability layer** for AI-driven systems.
It continuously checks external services (e.g. LLM bridges, APIs) and provides a clean status interface for diagnostics and automation.

---

## ⚙️ Core Features

| Feature | Description |
|---|---|
| 🌐 **Flask API** | Minimal, fast HTTP service for health endpoints |
| 📡 **Service Monitoring** | Tracks uptime and responsiveness of external AI services |
| 📊 **Status Endpoint** | Unified `/status` route for system health aggregation |
| 🧾 **Logging System** | Structured logs for debugging and audit trails |
| 🐳 **Docker Support** | Container-ready for scalable deployments |
| 🔁 **CI/CD Ready** | GitHub Actions integration for automated workflows |

---

## 🛠️ Tech Stack

- 🐍 Python 3.11+
- 🌐 Flask
- 📡 Requests (HTTP client)
- 🐳 Docker
- 🔄 GitHub Actions

---

## 🏗️ Architecture

```
[ Client / Dashboard ]
        ↓
Flask Cloud Monitor
        ↓
┌───────┴───────┐
│               │
AI Bridge    Nexus API
(Service A)  (Service B)
```

- Central node queries multiple services
- Aggregates responses into a unified health status
- Designed for easy extension (add more services effortlessly)

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
  pip install -r requirements.txt
```

### 2. Run the service
```bash
  python main.py
```

### 3. Access the monitoring endpoint
```
http://127.0.0.1:5000/status
```

### 🔍 Example Response
```json
{
  "status": "ok",
  "services": {
    "bridge": "online",
    "nexus": "offline"
  }
}
```

---

## 📦 Deployment

### Docker (recommended)
```bash
  docker build -t flask-cloud-monitor .
  docker run -p 5000:5000 flask-cloud-monitor
```

### Cloud Targets
- **AWS** — ECS / Lambda via container
- **Google Cloud Run**
- **Azure Container Apps**
- **Vercel** — via backend proxy

---

## 🧩 Extensibility

- Add new services in the monitoring config
- Integrate alerting (Slack, Email, Webhooks)
- Extend metrics (latency, error rates, retries)
- Plug into Prometheus / Grafana stack

---

## ⚡ Strategic Use Cases

- AI infrastructure monitoring (LLM pipelines)
- Microservice health aggregation
- DevOps observability layer for AI products
- Foundation for SaaS monitoring tools

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes (`git commit -m 'feat: add your idea'`)
4. Push to the branch (`git push origin feature/your-idea`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**JuNe aka RainbowDev** ([@junesdream](https://github.com/junesdream))
AI Systems • Full-Stack Development • Electronic Music