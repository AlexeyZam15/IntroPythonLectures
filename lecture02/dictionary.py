# словари
dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→',
    }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary:
#     print(k)

# for k in dictionary.values():
#     print(k)

# for k in dictionary:
#     print(dictionary[k])

print(dictionary['up'])
dictionary['up'] = 'up'
print(dictionary['up'])

del dictionary['up']

for item in dictionary:
    print(f'{item}: {dictionary[item]}')
