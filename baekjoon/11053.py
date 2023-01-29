n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(dp[n])
