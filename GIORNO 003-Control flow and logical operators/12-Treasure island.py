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

first_choice = input("You\'re at a cross road. Where do you want to go?\nType \"left\" or \"right\"")
if first_choice == "left".lower():
    second_choice = input("You\'ve come to a lake. There is an island int the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    if second_choice == "wait".lower():
            third_choice = input ("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blu. Which color do you chose?")
            if third_choice == "red".lower():
                print("Burned by fire.\nGame Over.")
            elif third_choice == "blu".lower():
                print("Eaten by beasts.\nGame Over.")
            elif third_choice == "yellow".lower():
                print("You win!")
            else:
                print("Game over")
    else:
            print ("Attacked by trout.\nGame over")
else:
    print ("Fall int a hole.\nGame over")

