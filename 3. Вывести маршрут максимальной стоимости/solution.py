import sys


def main():
    N, M = map(int, input().split())

    dp = [[0] * M for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]
    path = [[''] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            current_value = grid[i][j]
            if i == 0 and j == 0:
                dp[i][j] = current_value
            elif i == 0:
                dp[i][j] = dp[i][j-1] + current_value
                path[i][j] = 'R'
            elif j == 0:
                dp[i][j] = dp[i-1][j] + current_value
                path[i][j] = 'D'
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + current_value
                    path[i][j] = 'D'
                else:
                    dp[i][j] = dp[i][j-1] + current_value
                    path[i][j] = 'R'

    max_sum = dp[N-1][M-1]
    route = []
    i, j = N-1, M-1

    while i > 0 or j > 0:
        route.append(path[i][j])
        if path[i][j] == 'D':
            i -= 1
        else:
            j -= 1

    route.reverse()

    print(max_sum)
    print(''.join(route))

if __name__ == '__main__':
    main()
