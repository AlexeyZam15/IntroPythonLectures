# Функции

# Функции в python могут возвращать значение любого типа
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2
# print(f(arg))
# print(type(f(arg)))


def new_string(symbol, count=3):
    return symbol * count


def concatenatio(*params):
    res: str = ""
    for item in params:
        res += str(item)
    return res

# рекурсия


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
