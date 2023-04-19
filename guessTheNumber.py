import random

secretNumber = random.randint(1,20)
print('Ya zagadal chislo ot 1 do 20. U tebya 6 popytok')

for guessesTaken in range(1,7):
    print('Ugaday chislo')
    guess = int(input())

    if guess < secretNumber:
        print('Ya zagadal bolshee chislo')
    elif guess > secretNumber:
        print('Ya zagadal menshee chislo')
    else:
        break
if guess == secretNumber:
    print('Otlichno! Kolichestvo popytok: ' + str(guessesTaken) + '.')
else:
    print('Vam ne povezlo. Ya zagadal chsilo ' + str(secretNumber))
