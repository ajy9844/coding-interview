MAX_SIZE = 1001
n = int(input())

dp = [0] * MAX_SIZE
dp[1] = dp[3] = 1
dp[2] = 2

for i in range(4, n + 1):
    dp[i] = dp[i - 3] + 1

print("SK" if dp[n] % 2 != 0 else "CY")
