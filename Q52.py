def find_permuted(n):
    nList = [x for x in str(n)]
    for mult in range(2, 7):
        nListMult = [j for j in str(int(n*mult))]
        if len([i for i in nListMult if i not in nList]):
            return False
    return True

i = 0
while True:
    if find_permuted(i):
        print(i)
    i += 1