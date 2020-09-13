a, b = 100, 100
c = []
while a <= 1000:
    while b <= 1000:
        product = str(int(a*b))
        if product == product[::-1]:
            c.append([product, a, b])
        b += 1
    b = 100
    a += 1

print(c)