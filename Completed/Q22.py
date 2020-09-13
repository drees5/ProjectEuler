import time

start = time.time()
with open('Q22_names.txt') as data:
    names = data.read().split(',')

# Use map to calculate value of each name, then multiply value by index+1, finally calculate sum
print(sum([value * i for i, value in enumerate(list(map(lambda word: sum([ord(letter) - 64 for letter in word]), names)), 1)]))

end = time.time()
print(end - start)