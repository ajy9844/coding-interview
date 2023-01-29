n = int(input())
arr = [0] + list(map(int, input().split(" ")))
max_val = -1001

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
    max_val = max(dp[i], max_val)

print(max_val)
