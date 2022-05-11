import random
#generates a random number
mysterious_number = random.randint(0,1000)
print("Classic Guessing Game by Computer in Range (0 to 1000)")
#define max and min for computer for guess
min=0
max=1000
#store all the computer guessed try data 
story_try=[]
while True:
    #guess number by computer
    guess_number=random.randint(min,max)
    #add guess data in story_try 
    story_try.append(guess_number)
    print("Random Number Guessed by Computer is ",guess_number)
    #check the guess numebr if greater than or less than change the max and min value for new guess
    if(guess_number<mysterious_number):
        print("The correct answer is higher than the guess.")
        max=mysterious_number
        min=guess_number
    elif(guess_number>mysterious_number):
        print("The correct answer is lower than the guess.")
        max=guess_number
        min=mysterious_number
    else:
        #display the info ehen the mysterious number find by computer 
        print(story_try)
        print("Congratulations Computer guess the correct number ",guess_number)
        print("The number of  guesses Computer made : ",len(story_try))
        break

