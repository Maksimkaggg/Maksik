from itertools import product
k=0
for x in product('АНТИУТОПИЯ',repeat=16):
    s=''.join(x)

    if :
        k+=1
print(k)
'''from itertools import product
c = 0
for x in product('ЛЕТО', repeat = 4):
    s = ''.join(x)
    if s[0] == 'Л' or s[0] == 'Т':
        c += 1
print(c)'''

from itertools import product
c = 0
for x in product('АКРУ', repeat = 5):
    s = ''.join(x)
    c += 1
    if c == 350:
        print(s)
        break