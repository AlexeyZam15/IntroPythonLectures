text = 'съешь ещё этих мягких французских булок'

# help(text.istitle)

print(len(text)) ## длина строки = 39
print('ещё' in text) ## проверка элемента в строке = true
print(text.isdigit()) # false
print(text.islower()) # true
print(text.replace('eщё','ЕЩЁ')) # выполняется замена текста
print(text[-5]) # символы с конца текста - 5 символ с конца текста - б
print(text[2:5]) # вывод с 2 по 5 символ
print(text[6:-18])
print(text[0:len(text):6]) # вывод символа через каждые 6 символов с начала текста(0) до его конца(len(text))
print(text[::6]) # то же самое ^

# for c in text: # вывод каждого символа в тексте
#     print(c)