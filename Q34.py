import time

start = time.time()

factorials = {1: 1, 2: 2, 0: 1, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

def factorial(n, factorials):
    if n < 1:  # base case
        return 1
    else:
        if (n-1) not in factorials.keys():
            fac = factorial(n-1, factorials)
            factorials[n-1] = fac
        else:
            fac = factorials[n-1]
        returnNumber = n * fac  # recursive call
        if returnNumber not in factorials.keys():
            factorials[n] = returnNumber
        return returnNumber

for i in range(10**9):
    if sum([factorial(int(num), factorials) for num in str(i)]) == i:
        print(i)

end = time.time()

print(end-start)