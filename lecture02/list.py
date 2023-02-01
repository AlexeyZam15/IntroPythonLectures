# # списки
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# # значения меняются в обоих списках, т.к. list2 содержит ссылку на list1, а не копию
# list1[0] = 123
# list1[1] = 333
# print(list1)
# print(list2)

# pop извлекает последний элемент из списка
list1 = [1, 2, 3, 4, 5]
print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
print(list1.pop(2))
print(list1)
list1.insert(2, 11)
print(list1)
list1.append(11)
print(list1)