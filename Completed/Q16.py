import time
start = time.time()

print(sum([int(c) for c in str(int(2 ** 1000))]))
end = time.time()
print(end-start)