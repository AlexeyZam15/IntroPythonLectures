# # кортежи
# a = (3, 4, 41, 4)
# print(a)
# print(a[0])
# print(a[-1])
# print(a[-2])
# # кортежи не изменяются
# a[0] = 12

# t = ()
# print(type(t))
# #кортеж из 1 элемента
# t = (1,)
# print(type(t))
# #число
# t = (1)
# print(type(t))
# t = (28,9,1990)
# print(type(t))
# colors = ['red','green','blue123']
# print(colors)
# print(type(colors))
# t = tuple(colors)
# print(t)
# print(type(t))

# a = (3,4,5)
# # print(a)
# # print(a[0])

# for item in a:
#     print(item)

t = tuple(['red','green','blue123'])
print(t)
red, green, blue = t
print(f'r: {red} g:{green} b:{blue}')