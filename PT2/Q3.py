def knapsack(n, w, weights, values):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    weight_remaining = w
    for i in range(n, 0, -1):
        if dp[i][weight_remaining] != dp[i - 1][weight_remaining]:
            selected_items.append(i)
            weight_remaining -= weights[i - 1]

    return w - weight_remaining, selected_items[::-1]

with open("bag.inp", "r") as f:
    n, w = map(int, f.readline().split())
    weights = []
    values = []
    for _ in range(n):
        a, b = map(int, f.readline().split())
        weights.append(a)
        values.append(b)

remaining_weight, selected_items = knapsack(n, w, weights, values)
print(remaining_weight)
print(*selected_items)

