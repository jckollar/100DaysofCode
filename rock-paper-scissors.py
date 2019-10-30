import random

shapes = ["rock", "paper", "scissors"]
computer = random.choice(shapes)
# computer = shapes[random.randint(0,2)]
player = input("rock, paper or scissors? ")

if player == computer:
    print("It is a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Score! rock beats scissors!")
    if computer == "paper":
        print("Sorry, paper beats rock!")
elif player == "scissors":
    if computer == "rock":
        print("Sorry, rock beats scissors!")
    if computer == "paper":
        print("Score! scissors beats paper!")
elif player == "paper":
    if computer == "scissors":
        print("Sorry, scissors beats paper!")
    if computer == "rock":
        print("Score, paper beats rock")
