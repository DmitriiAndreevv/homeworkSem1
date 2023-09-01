print('Введите стороны треугольника')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a < b + c and b < a + c and c < a + b:
    print('такой треугольник у нас есть)')
    if a == b == c:
        print('стороны треугольника равные')
    elif a == b or b == c or a == c:
        print('это равнобедренный треугольник')
    else:
        print('треугольник разносторонний')
else:
    print('такого треугольника нет!')
