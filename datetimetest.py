import datetime

p = datetime.datetime.now()
n = str(p)
m = 0
nm = ''
while m < 19:
    nm += n[m]
    m += 1
print(nm)