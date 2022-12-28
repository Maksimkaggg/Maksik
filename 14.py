x = 4**2014 + 2**2015 - 8
s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))
'''for x in '012345678':
    for y in '012345678':
        a = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if a % 61 == 0:
            print(a // 61)
            break'''