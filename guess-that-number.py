import random

chances = 0
number = random.randint(0, 20)

while chances < 3:
    guessNumber = int(input('Guess a number...'))
    chances = chances + 1
    if guessNumber > number:
        print('Your guess is too high!')
    if guessNumber < number:
        print('Your guess is too low!')
    if guessNumber == number:
        print(number, 'is the winner guess!')
        break
