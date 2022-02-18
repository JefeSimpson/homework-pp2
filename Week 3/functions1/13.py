'''
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
This is how it should work when run in a terminal:
'''
import random

def guessTheNumber(): 
    name = input("Hello, What is your name?\n") 
    num = int(input("\n"+"Well, " + name + ", I am thinking of a number between 1 and 20.\n" + "Take a guess.\n"))
    right_num = random.randint(1, 20)
    count = 1
    while num != right_num: 
        if right_num > num and right_num != num: 
            num = int(input("\n" + "Your guess is too low.\n" + "Take a guess.\n"))
        elif right_num < num and right_num != num:
            num = int(input("\n" + "Your guess is too high.\n" + "Take a guess.\n"))
        count += 1    
    else: 
        print("\n" + "Good job, " + name + "! You guessed my number in " + str(count) + " guesses!")


guessTheNumber()