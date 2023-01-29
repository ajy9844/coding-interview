MAX_SIZE = 30
t = int(input())

dp = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

for i in range(1, MAX_SIZE):
    for j in range(1, MAX_SIZE):
        if i >= j:
            dp[i][j] = 1
        elif i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])
