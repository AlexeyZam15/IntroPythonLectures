import functions as f

# print(functions.f(1))

# print(f.f(1))

# print(f.new_string('!', 5))
# print(f.new_string('!'))
# print(f.new_string(4))

# print(f.concatenatio('a', 's', 'd', 'w'))
# print(f.concatenatio('a', '1'))
# print(f.concatenatio('1', '2', '3', '4'))

list1 = []
for e in range(1, 10):
    list1.append(f.fib(e))
print(list1)
