import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    graph = defaultdict(list)

    for g1, g2 in arr:
        graph[g1].append(g2)
        graph[g2].append(g1)

    color = [0] * (n + 1)

    def dfs(node, c):
        color[node] = c

        for neighbor in graph[node]:
            if color[neighbor] == 0:
                if not dfs(neighbor, -c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                break
    else:
        print("YES")

if __name__ == '__main__':
    main()
