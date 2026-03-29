import random

class FinanceEnv:
    def __init__(self):
        self.initial_balance = 10000
        self.initial_savings = 2000
        self.initial_expenses = 5000
        self.reset()

    def reset(self):
        self.balance = self.initial_balance
        self.savings = self.initial_savings
        self.expenses = self.initial_expenses
        self.steps = 0

        return self.state()

    def state(self):
        return {
            "balance": self.balance,
            "savings": self.savings,
            "expenses": self.expenses,
            "steps": self.steps
        }

    def step(self, action):
        reward = 0

        if action == "save":
            self.savings += 1000
            self.balance -= 500
            reward += 0.5

        elif action == "spend":
            self.expenses += 1000
            self.balance -= 1000
            reward -= 0.5

        elif action == "invest":
            if random.random() < 0.8:
                self.balance += 1500
                reward += 0.3
            else:
                self.balance -= 1000
                reward -= 0.3

        self.steps += 1

        done = self.steps >= 10

        return self.state(), reward, done, {}