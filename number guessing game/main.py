"""Number Guessing Game
This is a simple and fun game where you try to guess a secret number within a range of 50 to 100 in 5 attempts.
"""
"""logic building
1. Generate a random number range from 50 and 100
2. Get the user's guess
3. Check if the guess is correct
4. If the guess is higher,prompt the user to guess lower
5. If the guess is lower, prompt the user to guess higher
6 if user is righy, print a congratulatory message
"""
import random
print("Welcome to the Number Guessing Game!/n guess the number between 50 and 100.")

guess_counter=0
number_guess=random.randrange(50,100) #generate a random number between 50 and 100
chances=5
while guess_counter<chances:
    guess_counter+=1

    my_guess=int(input("Enter your guess: "))
    if my_guess == number_guess:
        print(f"Congratulations! You have guessed the number correctly. It's {number_guess}")
        break
    elif my_guess < number_guess:
        print("Your guess is too low. Try again.")
    elif my_guess > number_guess:
        print("Your guess is too high. Try again.")

if guess_counter == chances:
    print("Sorry! You have run out of chances.")
print(f"The number was {number_guess}")     
"""the reason for while loop is that we have to generate loop upto certain time like 5 or 3 times"""