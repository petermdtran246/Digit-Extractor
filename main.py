def Digits(n):
    while n > 0:
        digit = n % 10
        n = n // 10
        print(digit)

n = int(input('Enter n: '))
Digits(n)


