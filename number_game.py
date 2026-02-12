# Name: John Scarrow
# Date: 2/11/2026
# Description: A number guessing game where the computer picks a random
#              number between 1 and 10 and the user has 5 tries to guess it.

import random
import time
import os


# Generate a random number between 1 and 20
game_range = 0,20

user_guesses = []
computer_guesses = []

secret_number = random.randint(game_range[0], game_range[1])
user_secret_number = -1
print("Welcome to the Number Guessing Game! \n You are going to play against the computer to see who can guess the opponants number first.")
print(f"Pick a number between {game_range[0]} and {game_range[1]} for me to guess.")
while user_secret_number < game_range[0] or user_secret_number > game_range[1]:
    user_secret_number = int(input("Enter your number: "))
    if user_secret_number < game_range[0] or user_secret_number > game_range[1]:
        print(f"Please enter a number between {game_range[0]} and {game_range[1]}.")

# Prompt the user for their guess
print(f"I'm thinking of a number between {game_range[0]} and {game_range[1]}.")


game_running = True
round = 1

# Loop till the game is over
while game_running:
    wait_time = 1
    time.sleep(wait_time)

    last_guess_direction = ["Too low", "Too high"]

    # User last guesses
    if user_guesses != []:
        # if user_guesses[-1] > 0:
        #     print(f"Your last guess was {last_guess_direction[0]}")
        # else:
        #     print(f"Your last guess was {last_guess_direction[1]}")
        display_user_guesses = user_guesses.copy()
        for i, guess in display_user_guesses:
            if guess < 0:
                guess = guess * (-1)
        print(f"You have guessed {display_user_guesses}")

    # Prompt the user for their guess
    guess = int(input(f"Round {round} - Enter your guess: "))

    if guess == secret_number:
        # User guessed correctly
        game_running = False
        if user_guesses == []:
            print("WOW you beat the computer in the first round!")
            break
        print(f"\n\n\nCongratulations! You won! You guessed {user_guesses}. You guessed {secret_number} in on round {round}!\n")
        print("Computer guesses: ", computer_guesses, "                Your secret number: ", user_secret_number)
        break
    elif guess < secret_number:
        # Guess was too low
        print(f"Too low!")
        user_guess = guess * (-1)
        user_guesses.append([last_guess_direction[0], guess])
    else:
        # Guess was too high
        print(f"Too high!")
        user_guesses.append([last_guess_direction[1], guess])

    time.sleep(wait_time)

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #Computer takes a turn
    if computer_guesses == []:
        computer_guess = random.randint(game_range[0], game_range[1])
    elif computer_guesses [-1][1] > 0:
        computer_guess = random.randint(game_range[0], computer_guesses[-1][1])
    else:
        computer_guess = random.randint(computer_guesses[-1][1], game_range[1])

    # Computer last guesses
    if computer_guesses != []:
        # if computer_guesses[-1] > 0:
        #     print(f"The computer last guess was {last_guess_direction[0]}")
        # else:
        #     print(f"The computer last guess was {last_guess_direction[1]}")
        display_computer_guesses = computer_guesses.copy()
        for i, guess in display_computer_guesses:
            if guess < 0:
                guess = guess * (-1)
        print(f"The computer has guessed {display_computer_guesses}")

    # Print the computer's guess
    print(f"The computer guessed {computer_guess}")

    if computer_guess == user_secret_number:
        game_running = False
        # Computer guessed correctly
        if computer_guesses == []:
            print("WOW the computer beat you in the first round!")
            break
        print(f"\n\n\nThe computer beat you! The computer guessed {computer_guesses}. Computer guessed {user_secret_number} in on round {round}!")
        print("Your guesses: ", user_guesses, "                Computers secret number: ", user_secret_number)
        break
    elif computer_guess < user_secret_number:
        # Computer guess was too low
        print(f"The computer guessed {computer_guess} and it was too low!")
        computer_guess == computer_guess * (-1)
        computer_guesses.append([last_guess_direction[0], computer_guess])
    else:
        # Computer guess was too high
        print(f"The computer guessed {computer_guess} and it was too high!")
        computer_guesses.append([last_guess_direction[1], computer_guess])


    # Increment the attempt counter
    round += 1

    # Check if the user has reached the maximum number of attempts
    # if attempt == 5:
    #     print("You have reached the maximum number of attempts. The game is over.")
    #     break