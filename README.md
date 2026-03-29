---
title: Finance OpenEnv
emoji: 💰
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# 💰 Finance OpenEnv Environment

## Description
This project simulates personal finance decision-making where an AI agent manages:
- balance
- savings
- expenses

The goal is to model realistic financial behavior and decision-making.

---

## Actions

- save → increases savings
- spend → increases expenses
- invest → risky balance growth

---

## Intelligent Policy

The agent follows a state-aware strategy:

- Builds a savings safety net first
- Avoids risky investment after losses
- Invests only when financially stable
- Maintains balance control

---

## State

{
  "balance": int,
  "savings": int,
  "expenses": int,
  "steps": int
}

---

## Tasks

Easy:
- Reach savings ≥ 5000

Medium:
- Reach balance ≥ 20000

Hard:
- Maximize total wealth ≥ 30000

---

## Reward Logic

- Saving → positive reward
- Spending → negative reward
- Investment → variable reward (risk/reward tradeoff)

---

## API Endpoints

- GET /reset → reset environment
- GET /state → current state
- POST /step?action=save → perform action

---

## Run

python3 inference.py

---

## Deployment

https://deekshithaaa-finance-openenv.hf.space

---

## Project Structure

env/
 ├── environment.py
 ├── tasks.py
 ├── grader.py

app.py
inference.py
Dockerfile
requirements.txt
openenv.yaml
README.md

---

## Evaluation Ready

- OpenEnv compliant
- Working API endpoints
- Docker deployment successful
- Inference script reproducible
- Tasks with grading implemented

---

## Author

Deekshitha Puppala
