# Finance OpenEnv Environment

## Description
This environment simulates personal finance decision making where an AI agent manages balance, savings, and expenses.

## Actions
- save: increases savings
- spend: increases expenses
- invest: risky balance growth

## State
- balance
- savings
- expenses
- steps

## Tasks
- Easy: Reach savings >= 5000
- Medium: Reach balance >= 20000
- Hard: Maximize total wealth >= 30000

## Reward Logic
- Saving gives positive reward
- Spending gives negative reward
- Investment gives variable reward

## How to Run
```bash
python3 inference.py