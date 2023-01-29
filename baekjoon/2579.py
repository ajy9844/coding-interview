n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = arr[i]
    elif i == 2:
        dp[i] = arr[i] + arr[i - 1]
    else:
        dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])

print(dp[n])
