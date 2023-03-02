"""print('x', 'y', 'z', 'w')#  ^ and
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x and y and not(z)) == (y or z or not(w)):
                    print(x, y, z, w)"""

# лучший код


from itertools import *


def f(x, y, z, w):
    return not (y <= x) or (z <= w) or not z


for a in product([0, 1], repeat=7):
    table = [(a[0], 0, a[1], a[2]),
             (0, 1, a[3], a[4]),
             (1, a[5], a[6], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
