x = 4**2014 + 2**2015 - 8
s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))