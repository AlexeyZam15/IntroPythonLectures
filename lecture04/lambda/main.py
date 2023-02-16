# def calc2(x):
#     return x * 10
#
#
# def math(op, x):
#     print(op(x))
#
#
# math(calc2, 10)  # 100


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


# В op закладывается функция
def calc(op, a, b):
    print(op(a, b))


# calc(mult, 4, 5)  # 20

# # Псевдоним для функции sum
# f = sum
# calc(f, 4, 5)  # 9

# def sum(x, y):
#     return x + y
# # ⇔ (равносильно)
# sum = lambda x, y: x + y
# print(sum(1, 9))

# лямбда функция без имени
calc(lambda x, y: x + y, 4, 5)
