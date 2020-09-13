# https://projecteuler.net/problem=2

a, b = 1, 1
sum = 0

while a < 4*10**6:
    if a % 2 == 0:
        sum += a
    a, b = b, a+b

print(sum)