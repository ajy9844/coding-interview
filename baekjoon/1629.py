def pow(x, y, m):
    if y == 1:
        return x
    elif y % 2 == 0:
        k = pow(x, y // 2, m)
        return k * k % m
    elif y % 2 == 1:
        k = pow(x, y // 2, m)
        return x * k * k % m


a, b, c = map(int, input().split())
print(pow(a, b, c) % c)
