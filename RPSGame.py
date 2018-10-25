from random import randint

#avaikable weapons => Store this is an array
choices = ["Rock","Paper","Scissors"]

# Make the computer pick one item at random
computer_choice = choices[randint(0, 2)]

#Show the computer's choice in the terminal window
print("Computer chooses: ",computer_choice)