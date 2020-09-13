import time
start = time.time()

def isPalindrome(n):
    binary = str(bin(n).strip("0b"))
    num = str(n)
    if num != (num)[::-1]:
        return False
    if bin(n)[2:] != bin(n)[2:][::-1]:
        return False
    return True


print(sum([i for i in range(1, 10 ** 6, 2) if isPalindrome(i)]))

end = time.time()

print(end-start)