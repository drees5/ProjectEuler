i = 20
nums = range(2, 21)


def moudlus(n):
    for x in nums:
        if n % x:
            return False
    return True


while True:
    if moudlus(i): print(i)
    i += 2
