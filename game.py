import random
choices=["rock","paper","scissors"]
rock=choices[0]
paper=choices[1]
scissors=choices[2]
print("Well come to rock,paper, scissors game. To finish the game press q")
while True:
    choose = input("rock or paper or scissors ? ")
    computer = random.choice(choices)
    if choose==rock:
        if computer==rock:
            print("Computer's choices: rock Result: Tie")
        elif computer==paper:
            print("Computer's choices: paper You losted")
        else:
            print("Computer's choices: scissors Result: You won")
    if choose==paper:
        if computer==rock:
            print("Computer's choices: rock Result: You won")
        elif computer==paper:
            print("Computer's choices: paper Result: Tie")
        else:
            print("Computer's choices: scissors Result: You losted")
    if choose==scissors:
        if computer==rock:
            print("Computer's choices: rock Result: You losted")
        elif computer==paper:
            print("Computer's choices: paper Result: You won")
        else:
            print("Computer's choices: scissors Result: Tie")
        if choose=='q':
            print("Quiting...")
            break
