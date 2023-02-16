# 1. В списке хранятся числа.
# 2. Составить новый список из случайных чисел первого списка

from random import randint


def random_numbers_list(f, list1: list):
    return [f(list1) for x in list1]


def random_number(list1):
    return list1[randint(0, len(list1) - 1)]


def random_numbers(list1: list):
    return [random_number(list1) for x in list1]


def function(f):
    return f


numbers = [1, 2, 3, 5, 8, 15, 23, 38]
print('Изначальный массив \n', numbers, sep='')

res = random_numbers_list(lambda list1: list1[randint(0, len(list1) - 1)], numbers)
# res = random_numbers_list(lambda list1: random_number(list1), numbers)

# res = random_numbers(numbers)
# res = [random_number(numbers) for x in numbers]
print('Массив из случайных чисел изначального массива \n', res, sep='')
