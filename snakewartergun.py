#  Sanke Water Gun Game

import random
print("Let's play SNAKE🐍 WATER🌊 GUN🔫")


def wingame(you, comp):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True,
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


i = 0
score = 0
while(i == 0):
    ra = random.randint(1, 3)
    if ra == 1:
        comp = 's'
    elif ra == 2:
        comp = 'w'
    elif ra == 3:
        comp = 'g'
    you = input("Your Turn: \n Snake(s)? \n Water(w)? \n Gun(g)? ")
    print("Computer Turn:\n Snake(s)? \n Water(w)? \n Gun(g)?")
    print(f'You Chose {you}')
    print(f'Computer Chose {comp}')
    if wingame(you, comp) == None:
        print('Tie')

    if wingame(you, comp) == True:
        print("You Win")
        score = score+5
        print("your score is ", score)

    else:
        print('You Lose!!')
    i = int(input('Continue(0) Exit(1)?'))
