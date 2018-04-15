STRATEGIES = []


def profit_strategy(strategy):
    STRATEGIES.append(strategy)
    return strategy


@profit_strategy
def plan_a(var_a, var_b):
    return var_a ** 2 / var_b


@profit_strategy
def plan_b(var_a, var_b):
    return (var_a + var_b) * 3


@profit_strategy
def plan_c(var_a, var_b):
    return var_a * var_b - 15


def max_profit(var_a, var_b):
    return max(strat(var_a, var_b) for strat in STRATEGIES)


if __name__ == "__main__":
    print(max_profit(10, 20))

