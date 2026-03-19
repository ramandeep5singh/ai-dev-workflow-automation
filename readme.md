# 🚀 AI Dev Workflow Automation

A modular AI-powered backend system that automates developer workflows using **MCP + n8n + Local LLMs (Ollama)**.

This project demonstrates how to build a **tool-based AI backend framework** with a unified API and extensible architecture.

---

## 🔧 Features

* Generate feature development tasks
* Generate unit tests from code
* Unified tool-based API (single endpoint → multiple tools)
* MCP integration (Claude Desktop compatible)
* Fully local setup (no paid APIs required)
* Structured JSON responses (consistent contract)

---

## 🧠 Architecture

```
Client (Claude / API)
        ↓
MCP Server (FastMCP - Python)
        ↓
n8n Webhook (Single Entry Point)
        ↓
Tool Router (Switch Node)
        ↓
Ollama (Local LLM)
        ↓
Response Formatter (Standardized Output)
        ↓
Client Response
```

---

## ⚙️ Tech Stack

* n8n – Workflow orchestration
* FastMCP (Python) – Tool interface layer
* Ollama – Local LLM (phi3 / llama3)
* Docker – n8n runtime
* Python – Backend logic
* JavaScript (n8n nodes) – Output processing

---

## 🧩 Tool-Based Design

Each capability is implemented as a **tool** with a shared contract.

### Request Format

```json
{
  "tool": "generate_feature_tasks",
  "input": {
    "feature_description": "Build login system"
  }
}
```

---

### Response Format

```json
{
  "tool": "generate_feature_tasks",
  "status": "success",
  "result": {
    "tasks": ["..."]
  }
}
```

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
docker run -it --rm -p 5678:5678 n8nio/n8n
```

---

### 5. Import Workflow

* Open: http://localhost:5678
* Import file: `ai-dev-workflow.json`
* Activate the workflow (Production mode)

---

### 6. Install & Run Ollama

```bash
ollama run phi3
```

Ensure Ollama is running in the background.

---

### 7. Run MCP Server

```bash
python mcp-servers/server.py
```

---

### 8. Configure Claude Desktop

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

```
http://localhost:5678/webhook/ai-dev-workflow
```

---

## 🧪 Example Requests

### Generate Feature Tasks

```json
{
  "tool": "generate_feature_tasks",
  "input": {
    "feature_description": "Build OAuth login system"
  }
}
```

---

### Generate Unit Tests

```json
{
  "tool": "generate_unit_tests",
  "input": {
    "code": "def add(a,b): return a+b"
  }
}
```

---

## 🧠 Key Concepts

* Tool-based architecture for AI systems
* Single entrypoint → multiple capabilities
* Structured input/output contracts
* LLM orchestration using n8n
* Post-processing for reliable outputs

---

## ⚠️ Limitations

* Local LLMs are slower than cloud models
* Smaller models (phi3) may produce inconsistent output
* Requires prompt tuning for better results
* No authentication (prototype stage)
* Not production-ready yet

---

## 💡 Future Improvements

* Add more tools (code review, refactoring, bug detection)
* Introduce persistent storage (logs/history)
* Add authentication layer
* Improve response reliability with better models
* Deploy as a cloud service

---

## 🧠 Summary

This project demonstrates how to build a **modular AI backend system** by combining:

* Workflow automation (n8n)
* Local LLM inference (Ollama)
* Tool orchestration (MCP)

into a scalable and extensible developer automation framework.

---
