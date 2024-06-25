import random
a=10
b=5
def check_level(lev):
    if lev =='easy':
        return a
    else:
        return b

def check_number(guess,ans,attem):
    if guess<ans:
        print('number is too low')
        return attem-1
    elif guess>ans:
        print('number is too high')
        return attem-1
    else:
        print(f'congratulation! you guess the number.number is {ans}')
        return attem-1




print('let me think of a number between 1 to 50')
answer=random.randint(1,50)
#print(answer)
level=input('choose level of difficulty as "easy" or "hard"')
attempts=(check_level(level))

guess_number=0
while guess_number!=answer and attempts!=0:
    print(f'you have {attempts} attempts to guess the number')
    guess_number=int(input('Guess the number'))

    attempts=check_number(guess_number,answer,attempts)
    if attempts==0:
        print('you loss,Better luck next time')




