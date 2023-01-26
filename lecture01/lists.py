# Списки
# list = list

# numbers = [1, 2, 3, 4, 5]
# print(type(numbers))

# ran = range(1, 6) # не список
# print(type(ran))

# numbers = list(ran) #приведение к типу list - список
# numbers = list(range(1, 6))
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len') # длина элементов списка
# print(numbers)
# for i in numbers:
#     i*=2 # умножение элементов списка на 2
#     print(i, end=' ')

colors = ['red', 'green', 'blue']

for e in colors:
    print(e, end=' ')
print()

for e in colors:
    print(e*2, end=' ')  # каждый строковый элемент дублируется
print()

colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # проверка списка - true
colors.remove('red')  # удалить элемент red

del colors[0]  # удалить первый элемент списка

for e in colors:
    print(e, end=' ')
