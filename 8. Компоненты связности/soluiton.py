import sys
from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())
    all_paths = [tuple(map(int, input().split())) for _ in range(m)]
    graph = defaultdict(list)

    for g1, g2 in all_paths:
        graph[g1].append(g2)
        graph[g2].append(g1)

    visited = set()
    components = []

    def dfs(start):
        queue = deque([start])
        visited.add(start)
        component = []

        while queue:
            vertex = queue.popleft()
            component.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return component

    for vertex in range(1, n + 1):
        if vertex not in visited:
            component = dfs(vertex)
            components.append(component)

    print(len(components))

    for component in components:
        print(len(component))
        print(*component)

if __name__ == '__main__':
    main()
