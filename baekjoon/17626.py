MAX_SIZE = 50001
n = int(input())

dp = [0] * MAX_SIZE
dp[1] = 1

for i in range(2, n + 1):
    x = int(i**0.5)
    if x**2 == i:
        dp[i] = 1
    else:
        dp[i] = dp[i - (x**2)] + 1
        for j in range(x - 1, 0, -1):
            dp[i] = min(dp[i - (j**2)] + 1, dp[i])

print(dp[n])
