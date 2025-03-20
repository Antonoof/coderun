import sys

def main():
    N, M = map(int, input().split())
    dp = [[0] * M for _ in range(N)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(M):
            if i > 1 and j > 0:
                dp[i][j] += dp[i-2][j-1]
            if i > 0 and j > 1:
                dp[i][j] += dp[i-1][j-2]

    print(dp[N-1][M-1])

if __name__ == '__main__':
    main()
