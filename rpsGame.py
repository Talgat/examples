import random, sys
print('Kamen, Nozhnitsy, Bumaga')

wins = 0
losses = 0
ties = 0

while True:
    print('%s pobed, %s pozrazheniy, %s nichih ' % (wins, losses, ties))
    while True:
        print('Viberete hod: (k) Kamen, (n) Nozhnitsy, (b) Bumaga, (e) Vyhod')
        playerMove = input()

        if playerMove == 'e':
            sys.exit()
        if playerMove == 'k' or playerMove == 'n' or playerMove == 'b':
            break
        print('Vvedite "k","n","b" ili "e"')
    if playerMove == 'k':
        print('Kamen i ...')
    elif playerMove == 'n':
        print('Nozhnitsy i ...')
    elif playerMove == 'b':
        print('Bumaga i ...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'k'
        print('Kamen')
    elif randomNumber == 2:
        computerMove = 'n'
        print('Nozhnitsy')
    elif randomNumber == 3:
        computerMove = 'b'
        print('Bumaga')
    #_________________________
    if playerMove == computerMove :
        print('Nichya!')
        ties = ties +1
    elif playerMove == 'k' and computerMove == 'n':
        print('Vy vyigrali!')
        wins = wins + 1
    elif playerMove == 'b' and computerMove == 'k':
        print('Vy vyigrali!')
        wins = wins + 1
    elif playerMove == 'n' and computerMove == 'b':
        print('Vy vyigrali!')
        wins = wins + 1
    elif playerMove == 'k' and computerMove == 'b':
        print('Vy proigrali!')
        losses = losses + 1
    elif playerMove == 'b' and computerMove == 'n':
        print('Vy proigrali!')
        losses = losses + 1
    elif playerMove == 'n' and computerMove == 'k':
        print('Vy proigrali!')
        losses = losses + 1

