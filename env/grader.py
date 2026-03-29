class FinanceGrader:

    @staticmethod
    def grade_easy(env):
        # target: savings = 5000
        return min(env.savings / 5000, 1.0)

    @staticmethod
    def grade_medium(env):
        # target: balance = 20000
        return min(env.balance / 20000, 1.0)

    @staticmethod
    def grade_hard(env):
        # target: total wealth = 30000
        total_wealth = env.balance + env.savings
        return min(total_wealth / 30000, 1.0)