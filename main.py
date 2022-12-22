# 15 задание
for a in range(1, 50):
    flag=0
    for x in range(1, 1000):
        if (((x%40==0)or(x%64 == 0))<=(x%a == 0)) == 0:
            flag = 1
            break
    if flag == 0:
        print(a)