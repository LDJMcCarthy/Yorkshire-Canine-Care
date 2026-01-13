# 2 players, human vs computer
# 3 options for player.
# different combinations of options.
# Game loop

import random

game = True
while game:
    options = ["Rock", "Paper", "Scissors"]
    print()
    print("Enter 1 for Rock")
    print("Enter 2 for Paper")
    print("Enter 3 for Scissors")
    print("Enter 9 to quit")

    try:
        print()
        H_option = int(input("->>>  ")) - 1

    except:
        print("Enter one of the options above.")

    if H_option == 8:
        print("Thank you for playing!")
        game = False
        exit()
    print()
    print("You have selected: " + options[H_option])
    C_option = random.randint(0, 2)
    print("Computer have selected: " + options[C_option])
    print()
    if H_option == C_option:
        print("DRAW!!!")
    elif H_option < C_option and C_option - H_option != 2:
        print("YOU LOSE!!!")
    elif H_option < C_option and C_option - H_option == 2:
        print("YOU WIN!!!")
    elif H_option > C_option and H_option - C_option != 2:
        print("YOU WIN!!!")
    elif H_option > C_option and H_option - C_option == 2:
        print("YOU LOSE!!!")
    print()
    print()
