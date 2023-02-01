# colors = ['red','green','blue123']
# data = open('file.txt','a')
# data.writelines(colors)
# data.write('\nLINE 12 \n')
# data.write('LINE 13 \n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()