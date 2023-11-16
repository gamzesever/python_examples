n1 = 153
n2 = n1
sum = 0
len = len(str(n1))

while n2 > 0:
    sum += (n2 % 10) ** len
    n2 = n2 // 10

if n1 == sum:
    print('arm')
else:
    print('not arm')