# http://radiusofcircle.blogspot.com

# importing time module
import time

# time at the start of execution
start = time.time()

# numbers copied as string
with open('Q67_triangle.txt') as data:
    number = data.read()
# splitting the number into a list
number = number.strip().split('\n')

# converting each and every list of strings to int
number = list(map(lambda row: [int(i) for i in row.split(' ')], [row for row in number]))

# counter for counting number of iterations
counter = 0

# for loop for bottom-up approach
for i in range(len(number) - 2, -1, -1):
    for j in range(len(number[i])):
        number[i][j] = number[i][j] + max(number[i + 1][j], number[i + 1][j + 1])
        counter += 1
    number.pop()

# printing the output
print('Found {} in {} iterations'.format(number[0][0], counter))

# time at the end of execution
end = time.time()

# printing the total time
print(end - start)
