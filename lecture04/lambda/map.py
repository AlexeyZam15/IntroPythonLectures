# Функция map() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с новыми объектами.

list1 = [x for x in range(1, 20)]
print(*list(map(lambda x: f'{x:3}', list1)))

list1 = list(map(lambda x: x + 10, list1))
print(*list(map(lambda x: f'{x:3}', list1)))
