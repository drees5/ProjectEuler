import math


def Divisors(n):
    # Note that this loop runs till square root
    sum = 0
    i = 1
    while i <= math.sqrt(n):

        if n % i == 0:

            # If divisors are equal, add only one
            if n / i == i:
                sum += i
            else:
                # Otherwise add both
                sum += i + int(n / i)
        i = i + 1
    sum -= n
    return sum


def Primes(n):
    sum, sieve = [], [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

prime = Primes(10000)

memoisation = []

ami_nums = []

for i in range(2, 10000):
    if i not in prime and i not in memoisation:
        da = Divisors(i)
        db = Divisors(da)
        memoisation.extend([da, db])
        if i == db:
            if da != db:
                ami_nums.extend([i, da])

print(sum(ami_nums))