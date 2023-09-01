from random import randint

LOW = 0
HIGH = 1000
Attempts = 10

num = randint(LOW, HIGH)

count = 1
while count <= Attempts:
    print(f'Попытка {count}.')
    nums = int(input('Введите число: '))

    if nums == num:
        print('Правильное число!')
        break

    elif num < nums:
        print(f'число меньше {nums}')
    else:
        print(f'число больше {nums}')
    count += 1
else:
    print('У вас закончились все попытки!')


