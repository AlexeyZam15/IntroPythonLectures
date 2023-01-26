# Функции

# Функции в python могут возвращать значение любого типа
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

arg = 2.3
print(f(arg))
print(type(f(arg)))

arg = 2
print(f(arg))
print(type(f(arg)))