import sys
from collections import defaultdict, deque


def main():
    n, m = map(int, input().split())
    stack = defaultdict(list)
    visited = set()
    queue = deque([1])
    visited.add(1)

    for _ in range(m):
        g1, g2 = map(int, input().split())

        stack[g1].append(g2)
        stack[g2].append(g1)

    while queue:
        vertex = queue.popleft()

        for neighbor in stack[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    component = sorted(visited)

    print(len(component))
    print(" ".join(map(str, component)))

if __name__ == '__main__':
    main()
