for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2==0:
        s= n2 + '00'
    else:
        s = n2 + '11'
    if int(s, 2) < 134:
        print(n)