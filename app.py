#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# import random library
import random

#create a minigame for rock paper scissors, the user should be warned when entering an invalid input, it should be able to play by rounds, and the user should be able to quit the game at any time and ask they user when they want to quit
# create a list of options for the user to choose from
options = ["rock", "paper", "scissors"]
# create a variable to store the user's choice
user_choice = ""
# create a variable to store the computer's choice
computer_choice = ""
# create a variable to store the user's score
user_score = 0
# create a variable to store the computer's score
computer_score = 0
# create a while loop to keep the game running until the user quits
while True:
    # ask the user for their choice
    user_choice = input("Choose rock, paper, or scissors: ")
    # check if the user wants to quit
    if user_choice == "quit":
        # break out of the loop
        break
    # check if the user's choice is valid
    if user_choice in options:
        # generate a random number between 0 and 2
        computer_choice = random.randint(0, 2)
        # assign the computer's choice based on the random number
        if computer_choice == 0:
            computer_choice = "rock"
        elif computer_choice == 1:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"
        # print the computer's choice
        print("Computer chose " + computer_choice)
        # check if the user and computer tied
        if user_choice == computer_choice:
            # print that the user and computer tied
            print("You tied!")
        # check if the user won
        elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
            # print that the user won
            print("You won!")
            # add one to the user's score
            user_score += 1
        # otherwise
        else:
            # print that the user lost
            print("You lost!")
            # add one to the computer's score
            computer_score += 1
        # print the user's score
        print("You: " + str(user_score))
        # print the computer's score
        print("Computer: " + str(computer_score))
    # otherwise
    else:
        # print that the user's choice is invalid
        print("Invalid choice!")

# print the final scores
print("Final scores:")
print("You: " + str(user_score))
print("Computer: " + str(computer_score))
# check if the user won
if user_score > computer_score:
    # print that the user won
    print("You won the game!")
    # check if the computer won
        elif computer_score > user_score:
