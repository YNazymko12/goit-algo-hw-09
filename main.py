import timeit

coins = [50, 25, 10, 5, 2, 1]

#Функція жадібного алгоритму для касової системи, яка видає решту покупцеві
def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount = amount % coin
    return result

print(f"Жадібний алгоритм: ",find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}


#Функція динамічного програмування для касової системи, яка видає решту покупцеві
def find_min_coins(amount):
    # Ініціалізація таблиці для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібно 0 монет

    # Таблиця для зберігання використаних монет
    coin_used = [-1] * (amount + 1)

    # Заповнення таблиці dp
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Якщо сума не може бути сформована з доступних монет
    if dp[amount] == float('inf'):
        return {}

    # Відновлення використаних монет
    result = {}
    i = amount
    while i > 0:
        coin = coin_used[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin

    return result


print(f"Динамічне програмування: ", find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}

# Порівняння часу виконання жадібного алгоритму та динамічного програмування
amounts = [15, 60, 113, 129, 130, 200, 500, 999, 1005]
results = []

for amount in amounts:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    results.append([amount, time_greedy, time_dp])

print("| Amount | Greedy Time (s) | DP Time (s) |")
print("|--------|-----------------|-------------|")
for result in results:
    print(f"| {result[0]:>6} | {result[1]:>15.8f} | {result[2]:>11.8f} |")

