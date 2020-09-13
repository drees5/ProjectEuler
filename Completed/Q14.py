# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# dictionary with all the values initialized to 0
dic = {n: 0 for n in range(1, 1000000)}

# Entering the values of 1 and 2
dic[1] = 1
dic[2] = 2

# for loop find find the size of collatz sequences
for n in range(3, 1000000, 1):

    # counter to count the size for each iteration
    counter = 0

    # original number
    original_number = n

    # while loop to do collatz iterations
    while n > 1:

        # check if the number is a previous sequence
        if n < original_number:
            # Size of collatz sequence for the iteration
            dic[original_number] = dic[n] + counter
            break

        # collatz sequence conditions
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1

# dic.values() will give the values of the dictionary
# list.index(some_number) will output the index
# of the number. As the index starts from 0
# we are adding one to the index.
print(list(dic.values()).index(max(dic.values())) + 1)

# time at the end of execution
end = time.time()

# printing the total time of execution
print(end - start)