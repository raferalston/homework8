#рисовалка
def painting():
    for i in pole:
        print(' '.join(i))

#создание поля
size = int(input())
pole = []
for i in range(size):
    pole = pole + [['_']*size]
#х - номер списка сверху вниз
x = 0
#у - номер элемента в списке слева направо
y = 0
#
progress = True

#создание крестика в заданных координатах
pole[x][y] = 'x'
painting()

#список того, что прога может
command_list = ['up', 'down', 'left','right','exit']


 #подьем крестика
def up(x,y):      
    pole[x][y] = '_'
    if x < 0:
        x = size - 1
    x -= 1
    pole[x][y] = 'x'
    painting()
    print(x,y)
    return x

 #спуск крестика
def down(x,y):
    pole[x][y] = '_'
    if x >= size - 1:
        x = -1
    x += 1
    pole[x][y] = 'x'
    painting()
    print(x,y)
    return x

 #крестик влево
def left(x,y):
    pole[x][y] = '_'
    if y < 0:
        y = size - 1
    y -= 1
    pole[x][y] = 'x'
    painting()
    print(x,y)
    return y

#крестик вправо
def right(x,y):
    pole[x][y] = '_'
    if y > size - 1:
        y = 0
    y = y + 1
    pole[x][y] = 'x'
    painting()
    print(x,y)
    return y

 #выход
def exit():
    progress = False
    return progress

#сама собственно программа
while progress == True:
    user_input = input()
    if user_input == 'up':
        x = up(x,y)
    if user_input == 'down':
        x = down(x,y)
    if user_input == 'left':
        y = left(x,y)
    if user_input == 'right':
        y = right(x,y)
    if user_input == 'exit':
        exit()
print('good bye')
