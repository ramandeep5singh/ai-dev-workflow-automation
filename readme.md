# 🚀 AI Dev Workflow Automation

A modular AI-powered backend system to automate developer tasks using **n8n + MCP + Local LLM (Ollama)**.

This project acts as a **prototype/template** for building AI-driven developer tools.

---

## 🔧 Features

* Generate feature development tasks
* Generate unit tests from code
* Single API → multiple tools (via routing)
* MCP integration with Claude Desktop
* Fully local setup (no paid APIs required)

---

## 🧠 Architecture

Client (Claude / API)
→ MCP Server (FastMCP - Python)
→ n8n Webhook (Single Workflow)
→ Switch (Routing)
→ Ollama (Local LLM)
→ Formatter → Merge → Response

---

## ⚙️ Tech Stack

* **n8n** – Workflow automation
* **FastMCP (Python)** – Tool layer
* **Ollama** – Local LLM (phi3 / llama3)
* **Docker** – n8n runtime
* **Git** – Version control

---

## 📦 Setup Guide (Local)

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd ai-dev-workflow-automation
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run n8n (Docker)

```bash
docker run -it --rm `
-p 5678:5678 `
n8nio/n8n
```

---

### 5. Import Workflow

* Open: http://localhost:5678
* Import file from:

```bash
ai-dev-workflow-automation/ai-dev-workflow.json
```

* Publish it for production

---

### 6. Install & Run Ollama

```bash
ollama run phi3
```

(ensure Ollama is running in background)

---

### 7. Run MCP Server

```bash
python mcp-servers/server.py
```

---

### 8. Configure Claude Desktop

Add MCP server config:

```json
{
  "dev-workflow-tools": {
    "command": "python",
    "args": ["C:/path-to-project/mcp-servers/server.py"]
  }
}
```

---

## 🔗 API Endpoint

```bash
http://localhost:5678/webhook/ai-dev-workflow
```

---

## 🧪 Example Requests

### Generate Feature Tasks

```json
{
  "action": "generate_feature_tasks",
  "data": {
    "feature": "Build OAuth login system"
  }
}
```

---

### Generate Unit Tests

```json
{
  "action": "generate_unit_tests",
  "data": {
    "code": "def add(a,b): return a+b"
  }
}
```

---

## 🧩 Key Learnings

* Building **multi-action workflows using n8n**
* Integrating **MCP server with Claude**
* Handling **LLM output formatting**
* Debugging **real-world integration issues**
* Designing **modular AI backend systems**

---

## ⚠️ Limitations

* Local LLMs are **slow compared to cloud models**
* Smaller models (phi3, llama3) may **hallucinate or produce inconsistent output**
* Requires **manual prompt tuning** for better results
* No authentication/security layer (prototype stage)
* Not production-ready yet (local-first system)

---

## 💡 Future Improvements

* Add more tools (code review, bug detection, refactoring)
* Improve prompt engineering for reliable outputs
* Add database for storing history/logs
* Deploy to cloud (public API)
* Add authentication & monitoring

---

## 🧠 Summary

This project is a **foundation for an AI-powered developer backend system**, demonstrating how to combine:

* Workflow automation
* Local LLMs
* Tool orchestration

into a unified API.

---
