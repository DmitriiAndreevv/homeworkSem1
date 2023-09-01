MAX = 100_000
MIN = 0

num = int(input(f'Введите число от 0 до 100_000: '))

div = 2
count = 0
if (num >= MIN and num <= 100_000):
    for i in range(div, num - 1):
        if (num % i == 0):
            count += 1
    if (count <= 0):
        print('Число простое')
    else:
        print('Число составное')
else:
    print('число не соответствует заданному диапазону чисел!')
