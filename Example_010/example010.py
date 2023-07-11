monets = input('Введите через пробел "0" (решка) и "1" (орел): ').split()
reshka = '0'
gerb = '1'
count_reshka = 0
count_orel = 0
for i in monets:
    if i=='0':
        count_reshka+=1
    else:
        count_orel+=1
if count_reshka>=count_orel:
    print(count_orel)
else:
    print(count_reshka)