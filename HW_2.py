#1
print('Введите положительную длину отрезков треугольника')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and a + c > b:
    print('Треугольник существует')
else:
    print('Треугольник не сущесвтует')
if a == b or b == c or a == c:
    print('Треугольник равнобедренный')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник разносторонний')

#2


