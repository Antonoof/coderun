import sys
from collections import defaultdict, deque

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    adj_list = defaultdict(list)
    # Количество входящих рёбер для каждой вершины
    in_degree = [0] * (N + 1)

    # Заполняем список смежности и подсчитываем входящие рёбра
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    # Очередь для вершин без входящих рёбер
    queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])

    # Результат топологической сортировки
    topo_order = []

    # Обрабатываем очередь
    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)

        # Уменьшаем степень входящих рёбер для всех смежных вершин
        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            # Если степень становится нулевой, добавляем вершину в очередь
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Проверяем, содержит ли результат все вершины
    if len(topo_order) == N:
        print(*topo_order)
    else:
        print(-1)

if __name__ == '__main__':
    main()
