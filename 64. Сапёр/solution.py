import sys

def main():
    n, m, k = map(int, input().split())
    res = [[0] * m for _ in range(n)]
    cords = ((0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1))

    def summer(i, j):
        res[i][j] = -1

        for x, y in cords:
            dx = x + i
            dy = y + j

            if 0 <= dx < n and 0 <= dy < m and res[dx][dy] >= 0:
                res[dx][dy] += 1

    for _ in range(k):
        i, j = map(int, input().split())
        summer(i - 1, j - 1)

    for i in range(n):
        for j in range(m):
            if res[i][j] >= 0:
                print(res[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

if __name__ == '__main__':
    main()
