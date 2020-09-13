# Use Sieve of Eratosthenes
from Completed.gen_primes import gen_primes

num = 600851475143
factors = []
for number in gen_primes():
    if num % number == 0:
        factors.append(number)
    elif (number * number) > num:
        break

print(factors)
