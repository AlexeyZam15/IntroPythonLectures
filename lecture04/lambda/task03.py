# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# numbers = [int(x) for x in input('Введите числа через пробел').split()]

data = '15 132 654 324 123 65 123'

data = list(map(int, data.split()))
# data = [int(x) for x in data.split()]
print(data)