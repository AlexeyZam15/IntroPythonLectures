# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in

# Операции с числами
a = 1 < 4 and 5 > 2
print(a)

# Сравнение строк
a = 'qwe'
b = 'qwe'
print(a == b)

# Операции со списками
a = [1, 2]
b = [1, 2]
print(a == b)

# Множественные неравенства
a = 1 < 3 < 5 < 10
print(a)

func = 1
T = 4
x = 2
print(func<T>(x))

# or ИЛИ дизъюнкция
f = 1 > 2 or 4 < 6
print(f)

# in Содержится в
f = [1,2,3,4]
print(f)
print(2 in f)
# not Отрицание
print(not 2 in f)

# проверка на чётность
is_odd = f[0] % 2 == 0
print(is_odd)

is_odd = not f[0] % 2 
print(is_odd)