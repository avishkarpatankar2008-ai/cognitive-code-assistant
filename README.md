---
title: Cognitive Code Assistant
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# 🧠 Cognitive Developer Assistant (OpenEnv)

## 🚀 Overview
This project simulates real-world developer workflows where an AI assistant:

- Detects when a developer is stuck
- Restores lost context after interruptions
- Simplifies overengineered code

---

## 🧩 Tasks

### 1. Easy — Stuck Detection
Detect when a developer is repeating the same failing loop and provide a helpful hint.

### 2. Medium — Context Recovery
Restore context after interruption and guide the developer to resume work.

### 3. Hard — Code Simplification
Identify overengineered code and suggest a simple Python solution.

---

## ⚙️ Action Space

- `hint`
- `restore_context`
- `simplify`
- `explain_error`

---

## 📊 Observation Space

- `code_snapshot`
- `errors`
- `progress_score`
- `context_lost`

---

## 🧮 Reward Design

- Correct action → +0.5  
- Helpful message → +0.3  
- Wrong action → -0.2  
- Rewards are clipped between 0 and 1  

---

## ▶️ How to Run

### Local:
```bash
pip install -r requirements.txt
python app.py
