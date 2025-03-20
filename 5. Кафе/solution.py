def main():
    # Чтение входных данных
    N = int(input())  # Количество дней
    costs = [int(input()) for _ in range(N)]  # Стоимость обедов для каждого дня

    # Максимальное количество купонов ограничено числом дней
    max_coupons = N + 1  # На случай, если все дни дают купоны

    # dp[i][c] - минимальная стоимость за первые i дней с c оставшимися купонами
    dp = [[float('inf')] * max_coupons for _ in range(N + 1)]
    prev = [[None] * max_coupons for _ in range(N + 1)]  # Для восстановления пути

    # Начальное состояние: на нулевой день затраты равны 0, купонов нет
    dp[0][0] = 0

    # Заполнение таблицы динамики
    for i in range(1, N + 1):
        cost = costs[i - 1]
        for c in range(max_coupons):
            if dp[i - 1][c] == float('inf'):
                continue  # Если предыдущее состояние недостижимо, пропускаем

            # Вариант 1: Платим за обед (получаем купон, если цена > 100)
            new_coupons = c + (1 if cost > 100 else 0)
            if new_coupons < max_coupons and dp[i][new_coupons] > dp[i - 1][c] + cost:
                dp[i][new_coupons] = dp[i - 1][c] + cost
                prev[i][new_coupons] = (i - 1, c, False)  # Не использовали купон

            # Вариант 2: Используем купон (если есть хотя бы один)
            if c > 0 and dp[i][c - 1] > dp[i - 1][c]:
                dp[i][c - 1] = dp[i - 1][c]
                prev[i][c - 1] = (i - 1, c, True)  # Использовали купон

    # Поиск оптимального результата
    min_cost = float('inf')
    best_c = -1
    for c in range(max_coupons):
        if dp[N][c] < min_cost or (dp[N][c] == min_cost and c > best_c):
            min_cost = dp[N][c]
            best_c = c

    # Восстановление пути (номеров дней, когда использовались купоны)
    used_days = []
    i, c = N, best_c
    while i > 0:
        prev_i, prev_c, used_coupon = prev[i][c]
        if used_coupon:
            used_days.append(i)
        i, c = prev_i, prev_c

    # Вывод результатов
    print(min_cost)  # Минимальная суммарная стоимость
    print(best_c, len(used_days))  # Количество оставшихся и использованных купонов
    for day in sorted(used_days):  # Вывод дней в порядке возрастания
        print(day)

if __name__ == '__main__':
    main()
