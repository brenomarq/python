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

direction = input("You're on a crossroad, do you want to proceed left or right? ")

if direction == "left":
    choice = input("You find a river, will you wait for a boat or swim? ")

    if choice == "wait":
        print("You crossed the river unharmed and on the other side you find a house with 3 rooms.")
        door = input("Which door will you choose? Red, yellow or blue? ")

        if door == "blue":
            print("The room is on fire!")
            print("GAME OVER!")
        elif door == "yellow":
            print("Congratulations, you found the hidden treasure!")
            print("YOU WIN!")
        elif door == "red":
            print("Oh, no! The room is full of fierce beasts.")
            print("GAME OVER!")
        else:
            print("GAME OVER!")

    else:
        print("Unfortunately, you were attacked by trouts.")
        print("GAME OVER!")
else:
    print("Unfortunately, you fell into a hole!")
    print("GAME OVER!")
