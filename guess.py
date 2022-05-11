import random 
#print instruction for user 
def instructions():
    print("Guess the secret number! Hint: It's an integer between 1 and 100...")
#get random integer between 1 to 100 
def randint():
    return random.randint(1, 100)
#main function for guessing game 
def main():
    #call randomint function 
    number = randint()
    #count the number of guess 
    guesses = 0
    #call the instruction function 
    instructions()
    #make infinit loop to guess the random number and count number of guess 
    while True:
        guesses += 1
        guess_number = int(input("What is your guess? "))
        if number > guess_number:
            print("Too low!")
        elif number > guess_number:
            print("Too high!")
        else :
            print("You guessed it! It took you {} guesses.".format(guesses))
            break
#call main function to start the game .
main()