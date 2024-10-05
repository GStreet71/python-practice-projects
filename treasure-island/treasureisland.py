print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def question1():
    selection = input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n").lower()
    if selection != "left" and selection != "right":
        selection = input("Invalid entry. Type \"left\" or \"right\": ")
    elif selection == "left":
        question2()
    else:
        print("You fell into a hole. Game Over.")

def question2():
    selection = input("You have come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if selection != "wait" and selection != "swim":
        selection = input("Invalid entry. Type \"wait\" or \"swim\": ")
    elif selection == "wait":
        question3()
    else:
        print("You got attacked by an angry trout. Game Over.")

def question3():
    selection = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
    if selection != "red" and selection != "yellow" and selection != "blue":
        print("You picked a door that doesn't exist. Game Over.")
    elif selection == "yellow":
        print("You found the treasure! You win!")
    elif selection == "red":
        print("It's a room full of fire. Game Over.")
    elif selection == "blue":
        print("You entered a room full of beasts. Game Over.")

question1()