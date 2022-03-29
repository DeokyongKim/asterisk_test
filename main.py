def print_TTT(l):
    for i in range(0, 3):
        for j in range(0, 3):
            print(l[i * 3 + j], end='')
            if j != 2:
                print('|', end='')
            else:
                print(' ')
        if i != 2:
            print('-----')


def isEnd(l):
    end = False
    winner = 'None'

    for i in range(3):
        if l[i * 3] != ' ' and l[i * 3] == l[i * 3 + 1] == l[i * 3 + 2]:
            end = True
            winner = l[i * 3]
        if l[i] != ' ' and l[i] == l[i + 3] == l[i + 6]:
            end = True
            winner = l[i]
    if l[0] != ' ' and l[0] == l[4] == l[8]:
        end = True
        winner = l[0]
    if l[2] != ' ' and l[2] == l[4] == l[6]:
        end = True
        winner = l[2]

    for i in l:
        if i == ' ':
            break
        if l.index(i) == len(l) - 1:
            end = True

    return end, winner


def computerTurn(l):
    if l[4] == ' ':
        return 4
    for i in range(3):
        if l[i * 3] == l[i * 3 + 1] == 'O' or l[i * 3] == l[i * 3 + 2] == 'O' or l[i * 3 + 1] == l[i * 3 + 2] == 'O':
            if l[i * 3] == ' ':
                return i * 3
            elif l[i * 3 + 1] == ' ':
                return i * 3 + 1
            elif l[i * 3 + 2] == ' ':
                return i * 3 + 2
        if l[i] == l[i + 3] == 'O' or l[i] == l[i + 6] == 'O' or l[i + 3] == l[i + 6] == 'O':
            if l[i] == ' ':
                return i
            elif l[i + 3] == ' ':
                return i + 3
            elif l[i + 6] == ' ':
                return i + 6
    if l[0] == l[4] == 'O' or l[0] == l[8] == 'O' or l[4] == l[8] == 'O':
        if l[0] == ' ':
            return 0
        elif l[4] == '0':
            return 4
        else:
            return 8
    if l[2] == l[4] == 'O' or l[2] == l[6] == 'O' or l[4] == l[6] == 'O':
        if l[2] == ' ':
            return 0
        elif l[4] == '0':
            return 4
        else:
            return 8

    for i in range(9):
        if l[i] == ' ':
            return i


game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
keep = True
coordi = 0
winner = {'O': 'You Win', 'X': 'You Lose'}

while (keep):
    print('Enter the coordinate: ')
    print('123')
    print('456')
    print('789')
    print('')

    coordi = int(input())
    coordi = coordi - 1

    while game[coordi] != ' ':
        print('Wrong input. Please type again.')
        coordi = int(input())
        coordi = coordi - 1

    game[coordi] = 'O'

    a, b = isEnd(game)

    if not a:
        game[computerTurn(game)] = 'X'

    a, b = isEnd(game)
    keep = not a

    print_TTT(game)
    if b != 'None':
        print(winner[b])

    if b == 'None' and a == True:
        print('Game End')

    print('==============================')
