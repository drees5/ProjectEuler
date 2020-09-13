import math


def triangle(n): return (n * (n + 1)) / 2  # Returns the nth triangle number


def Divisors(n):
    # Note that this loop runs till square root
    sum = 0
    i = 1
    while i <= math.sqrt(n):

        if n % i == 0:

            # If divisors are equal, add only one
            if n / i == i:
                sum += 1
            else:
                # Otherwise add both
                sum += 2
        i = i + 1
    return sum
num = 1
while True:
    if Divisors(triangle(num)) > 500:
        print(num, triangle(num))
    num += 1