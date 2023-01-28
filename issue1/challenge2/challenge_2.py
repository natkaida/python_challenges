n, m = list(map(int, input().split()))
s = 0
if m == 0:
    s = 1
elif m == 1:
    s = n
else:
    for d in range(1, n):
        s += (n - d) // (m - 1)
print(s)