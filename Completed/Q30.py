def fifth(n):
    return True if sum(int(digit) ** 5 for digit in str(n)) == n else False


i = 2
total = 0
list = []
while True:
    if fifth(i):
        total += i
        list.append(i)
    i += 1