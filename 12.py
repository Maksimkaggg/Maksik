s = '8' * 68
while '222' in s or '888' in s:
        s = s.replace('222', '8', 1)
        s = s.replace('888', '2', 1)
print(s)