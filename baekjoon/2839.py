MAX_SIZE = 5001
n = int(input())

dp = [-1] * MAX_SIZE
dp[3] = dp[5] = 1

for i in range(6, n + 1):
    if dp[i - 5] != -1:
        dp[i] = dp[i - 5] + 1
    else:
        if dp[i - 3] != -1:
            dp[i] = dp[i - 3] + 1

print(dp[n])
