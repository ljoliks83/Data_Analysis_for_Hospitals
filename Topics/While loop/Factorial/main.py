n = int(input())

if 0 < n <= 100:
    i = 1
    f = 1
    while i <= n:
        f *= i
        i += 1
    print(f)
elif n == 0:
    print(1)
else:
    print('The number must be between 0 and 100')
