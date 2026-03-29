class FinanceTasks:

    @staticmethod
    def easy_task(env):
        # Goal: increase savings to 5000
        return env.savings >= 5000

    @staticmethod
    def medium_task(env):
        # Goal: increase balance to 20000
        return env.balance >= 20000

    @staticmethod
    def hard_task(env):
        # Goal: maximize total wealth
        total_wealth = env.balance + env.savings
        return total_wealth >= 30000