import sys

def main():
    n, m, k = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(n)]
    arr2 = [list(map(int, input().split())) for _ in range(m)]
    res = [[0] * k for _ in range(n)]
    res2 = [[0] * n for _ in range(k)]

    for i in range(n):
        for j in range(k):
            for k2 in range(m):
                res[i][j] += arr1[i][k2] * arr2[k2][j]

    for i in range(n):
        for j in range(k):
            res2[j][i] = res[i][j]


    for rows in res2:
        print(*rows)

if __name__ == '__main__':
    main()
