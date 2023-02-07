matrix = [
    [' ', 0, 1, 2],
    [0, '-', '-', '-'],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
]

def matrix_(*args):
    for i in matrix:
        print(*i)
    return args

def play_1(one, two):
    if 0 < one > 2:
        print("Введите другую пару чисел")
        play_1(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif 0 < two > 2:
        print("Введите другую пару чисел")
        play_1(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif matrix[one + 1][two + 1] == 'o':
        print('Это место уже занято\n Повторите ввод')
        play_1(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif matrix[one + 1][two + 1] == 'x':
        print('Это место уже занято\n Повторите ввод')
        play_1(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif matrix[one + 1][two + 1] == 'o':
        print('Это место уже занято\n Повторите ввод')
        play_1(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))

    else:
        matrix[one + 1][two + 1] = 'x'

def play_2(one, two):
    if 0 < one > 2:
        print("Введите другую пару чисел")
        play_2(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif 0 < two > 2:
        print("Введите другую пару чисел")
        play_2(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif matrix[one + 1][two + 1] == 'x':
        print('Это место уже занято\n Повторите ввод')
        play_2(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    elif matrix[one + 1][two + 1] == 'o':
        print('Это место уже занято\n Повторите ввод')
        play_2(int(input('Введите число по горизонтали\n')), int(input('Введите число по вертикали\n')))
    else:
        matrix[one + 1][two + 1] = 'o'


print('Для старта игры нажмите Enter')
print('---')
y = input('Что бы получить справку по управлению введите "Y" ')
print('---')

if y == 'Y':
    print('Для управления необходимо вносить координаты от 0 до 2 по вертикали и горизонтали, на пересечении координат '
          'устанавливается "х" или "о"\n Игрок 1 ходит "х"\n Игрок 2 ходит "о"')

matrix_(matrix)

i = 0

while True:
    print('Игрок 1, Ваш ход')
    play_1(int(input('Введите значение по вертикали ')), int(input('Введите значение по горизонтали ')))
    matrix_(matrix)
    i += 1
    if matrix[1][1:] == ['x', 'x', 'x']:
        print('Выйграли крестики!')
        break
    elif matrix[2][1:] == ['x', 'x', 'x']:
        print('Выйграли крестики!')
        break
    elif matrix[3][1:] == ['x', 'x', 'x']:
         print('Выйграли крестики!')
         break
    elif matrix[1][1] == matrix[2][1] == matrix[3][1] == 'x':
         print('Выйграли крестики!')
         break
    elif matrix[1][2] == matrix[2][2] == matrix[3][2] == 'x':
         print('Выйграли крестики!')
         break
    elif matrix[1][3] == matrix[2][3] == matrix[3][3] == 'x':
        print('Выйграли крестики!')
        break
    elif matrix[1][1] == matrix[2][2] == matrix[3][3] == 'x':
        print('Выйграли крестики!')
        break
    elif matrix[1][3] == matrix[2][2] == matrix[3][1] == 'x':
        print('Выйграли крестики!')
        break
    if i == 9:
        print('Ничья')
        break
    print('Игрок 2, Ваш ход')
    play_2(int(input('Введите значение по вертикали ')), int(input('Введите значение по горизонтали ')))
    matrix_(matrix)
    i += 1
    if matrix[1][1:] == ['o', 'o', 'o']:
        print('Выйграли нолики!')
        break
    elif matrix[2][1:] == ['o', 'o', 'o']:
        print('Выйграли нолики!')
        break
    elif matrix[3][1:] == ['o', 'o', 'o']:
        print('Выйграли нолики!')
        break
    elif matrix[1][1] == matrix[2][1] == matrix[3][1] == 'o':
        print('Выйграли нолики!')
        break
    elif matrix[1][2] == matrix[2][2] == matrix[3][2] == 'o':
        print('Выйграли нолики!')
        break
    elif matrix[1][3] == matrix[2][3] == matrix[3][3] == 'o':
        print('Выйграли нолики!')
        break
    elif matrix[1][1] == matrix[2][2] == matrix[3][3] == 'o':
        print('Выйграли нолики!')
        break
    elif matrix[1][3] == matrix[2][2] == matrix[3][1] == 'o':
        print('Выйграли нолики!')
        break
