seq = [0, 1]
while len(str(seq[-1])) < 1000:
    seq.append(seq[-2] + seq[-1])
print(len(seq) - 1)
