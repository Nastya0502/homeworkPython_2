n = int(input('Введите число n: '))
k = 0
while 2**k<=n:
    print(2**k, end=' ')
    k+=1