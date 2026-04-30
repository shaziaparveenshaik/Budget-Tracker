def greedy_budget(expenses, budget):
    # Sort expenses based on priority (high → low)
    expenses.sort(key=lambda x: x[2], reverse=True)

    selected = []
    total_cost = 0

    for name, cost, priority in expenses:
        if total_cost + cost <= budget:
            selected.append((name, cost))
            total_cost += cost

    return selected, total_cost