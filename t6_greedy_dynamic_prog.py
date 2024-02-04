def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return {"selected_items": selected_items, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = items[list(items.keys())[i - 1]]["cost"]
            calories = items[list(items.keys())[i - 1]]["calories"]

            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    total_calories = dp[n][budget]
    remaining_budget = budget

    for i in range(n, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            selected_items.append(list(items.keys())[i - 1])
            remaining_budget -= items[list(items.keys())[i - 1]]["cost"]

    return {"selected_items": selected_items[::-1], "total_cost": budget - remaining_budget, "total_calories": total_calories}


# Задані дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик функцій та вивід результатів
print("Greedy Algorithm Result:")
print(greedy_algorithm(items, budget))
print("\nDynamic Programming Result:")
print(dynamic_programming(items, budget))
