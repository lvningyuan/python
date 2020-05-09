import random
secret = random.randint(1,10)
temp =  input('game start , please input')
guess = int(temp)
x = 1;
if guess==secret:
    print('you win !!')
    print('you are very bright!')
    print('game over')
else:
    while guess != secret and x <=3:
        x += 1;
        temp =  input('not right ,please input again')
        guess = int(temp)
        if guess == secret:
            print('you win !!')
            print('you are very bright!')
        else:
            if guess > secret:
                print('too big')
            else:
                print('too small')
        print('game over')

