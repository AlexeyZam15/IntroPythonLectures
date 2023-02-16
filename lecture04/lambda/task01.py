# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# def filter_even_numbers(list1: list):
#     r_list = []
#     for i in list1:
#         if i % 2 == 0:
#             r_list.append(i)
#     return r_list
#
#
# numbers = [1, 2, 3, 5, 8, 15, 23, 38]
# print('Изначальный массив \n', numbers, sep='')
#
# even_numbers = filter_even_numbers(numbers)
# print('Чётные числа \n', even_numbers, sep='')
#
# square_pairs = [(i, i*i) for i in even_numbers]
# print(square_pairs)

# def select(f, col):
#     return [f(x) for x in col]
# то же самое что функция map

def where(f, col):
    return [x for x in col if f(x)]
# то же самое что функция filter

data = [1, 2, 3, 5, 8, 15, 23, 38]
print('Изначальный массив \n', data, sep='')
# res = select(int, data)
# res = map(int, data)

# res = where(lambda x: x % 2 == 0, data)
res = list(filter(lambda x: x % 2 == 0, data))
# res = where(lambda x: x % 2 == 0, res)
# res = filter(lambda x: x % 2 == 0, res)
print('Чётные числа \n', res, sep='')  # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
res = list(map(lambda x: (x, x ** 2), res))
# res = [(x, x ** 2) for x in res]
print('Квадратные пары \n', res, sep='')
