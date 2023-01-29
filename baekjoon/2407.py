ans = 1
n, m = map(int, input().split())

if m > n // 2:
    m = n - m

for i in range(1, m + 1):
    ans = ans * n // i
    n -= 1

print(ans)
