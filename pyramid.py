n = int(input("how many lines you want in your program"))
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2*i + 1))