#
#        project :Bulls and Cows.py
#        author : Angela Toscano-Mendez <atoscano2718086@woonsocketschools.com>
#        author : Kristina Xayachit <kxayachit2607064@woonsocketschools.com>
#        author : Natalie Taylor <ntaylor2701004@woonsocketschools.com >
#        date written: 10/10/2024
#
#   description: We're creating Bulls and Cows game where you 10 tries

print()
#  i like lizards man. 🦎❤️
# explaning the what the game is to the players

print(""" Lizards, Geckos and mice is a code-breaking paper-and-pencil game for two or more players.
 The game is played in turns by two opponents who aim to decipher the other's secret code by trial and error.
""")

print()

# explaining the rules of the game to players
print(""" In this game The first player is the Zoo keeper. 
They secretly choose a three digit number using the numbers zero to 9 with no duplicates. 
The second player, the Visitor, gets 10 tries to guess the secret number. After each guess, the Zoo keeper “scores” using the following code:

Lizards: 	One digit in your guess is correct and in the correct position of the secret code. 
Geckos:	    One digit of your guess is present in the secret code, but in the wrong position. If you get three Geckos, your guess has all the correct digits, but all in the wrong place!
Mice:	    None of the digits in your guess are in the secret code. 

You'll only get 10 attempts and if you don't get it in those 10 guesses you'll lose!
""")
#lizards geckos and mice
import random
print()

zooKeeper = input("Zoo keeper, what is your name?(or type C for computer): ")
if zooKeeper == "C":
    code = random.randint(100, 999)
    guess = -1
    while guess != code:
        guess = int(input("Enter your guess: "))
        if guess < code:
            print("Higher!")
        elif guess > code:
            print("Lower!")
        else:
            print("Congratulations! You guessed the code:", code)
else:
    code = input("Now enter the secret passcode, three-digit code (no duplicates): ")

    print()

    visitor = input("What is your name Visitor?: ")

    hasWon = False
    numberOfGuesses = 0
    while hasWon is False :

        print()
        guess = input("Take your guess visitor: ")
        numberOfGuesses += 1

        # Have Player 1 score Player 2's guess.
        score = input("Now the zooKeeper will score your guess: ")

        if score == "LLL":
            print(f"good job your guess {guess} is correctly! You won in {numberOfGuesses} guesses.")

            hasWon = True
        else:
            print(f"Thats not it, your guess was :  {guess} and you scored: {score}. You have {10-numberOfGuesses} left.")

