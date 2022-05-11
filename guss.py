import random 
#print instruction for user 
def instructions():
    print("Guess the secret number! Hint: It's an integer between 0 and 10...")
#get random integer between 0 to 10  
def randint():
    return random.randint(0, 10)
#main function for guessing game 
def main():
    #call randomint function 
    number = randint()
    #count the number of guess 
    guesses = 0
    #call the instruction function to print details 
    instructions()
    #make infinit loop to guess the random number and count number of guess 
    ch ="Y"
    while ch !="N":
        guess_number = int(input("Enter number: "))
        if guess_number > 9 :
            print("Input again")
            continue
        if number != guess_number:
            print("Better luck next time ")
        else :
            print("Hurray you have won")
        ch = input("Play more if yes, write Y else N ")

#call main function to start the game .
main()
