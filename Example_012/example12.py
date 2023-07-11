summ_numbers = int(input('Введите сумму чисел x и y: '))
multiplication_numbers = int(input('Введите произведение чисел x и y: '))
x = 0
y = 0
for i in range(summ_numbers):
    for j in range(summ_numbers):
        if i+j == summ_numbers:
            if i*j == multiplication_numbers:
                x =i
                y = j
print(f"x = {x}, y = {y}")