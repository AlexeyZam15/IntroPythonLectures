# # множества, содержат уникальные элементы
# colors = {'red', 'green', 'blue'}
# print(colors)
# print(type(colors))
# colors.add('red')  # не добавляется т.к. уже есть
# print(colors)
# colors.add('gray')
# print(colors)
# # удаляет элемент, если элемента нет - ошибка
# colors.remove('gray')
# print(colors)
# # удаляет элемент, если элемента нет - ничего
# colors.discard('red')
# print(colors)
# # очистка множества
# colors.clear()
# print(colors)

a = {1, 2, 3, 5, 8}
print(a)
b = {2, 5, 8, 13, 21}
print(b)
# копирование множества
c = a.copy()
print(c)
# объединение множеств
u = a.union(b)
print(u)
# пересечение
i = a.intersection(b)
print(i)
# разница a - b
dl = a.difference(b)
print(dl)
# разница b - a
dr = b.difference(a)
print(dr)

# q = a.union(b).difference(a.intersection(b))
q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)

# неизменяемое множество
s = frozenset(a)
