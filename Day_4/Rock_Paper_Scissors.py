# Random Module
###############

# import random
# eg:- random.randint(1,10) ====> generates a random number between 1 and 10.
###############

# Python Lists
###############

# A way of storing related datas in a single container.
# eg:- fruits = [item1, item2]
# The items inside a list can be of different data types.
# eg:- list_of_fruits = ["Apple", "Pear" , "Watermelon"]
# eg:- list_of_fruits.append("grapes")
# eg:- list_of_fruits.extend(["strawberry, "orange", "coconut"])

# You can create a list of lists

# eg:- fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1]) ====> Kale

###############
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_choices = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_choices[user_choice])
    
print("The computer chose :")

computer_choice = random.randint(0,2)

print(game_choices[computer_choice])
    
if user_choice == computer_choice :
    
    print("Draw!")

elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2)  or (user_choice == 2 and computer_choice == 0) :
    
    print("You lose!")
    
else :
    
    print("You win!")