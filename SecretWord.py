#create a main funtion for the game  
def main():
    #make a while loop with true condition  to play game again by your choice 
    while True:
        #get the player 1 word as input 
        word = input("Player 1:  Please enter a 5 letter word  ")
        #check the length of word 
        if len(word) !=5:
            print("Incorrect length")
            continue
        #print msg and get the input of player 2
        print("\nPlayer 2 - it is your turn to guess letters!")
        #make a var for count correct guess of player 2
        correct = 0
        # for loop for taking five letter input from player 2
        for i in range(5):
            let = input("Please enter a letter :")
            #check condition 
            if len(let) != 1 or let.isalpha() == False:
                #while loop to get correct input form player 2
                while True:
                    let = input("Incorrect input, please enter a letter :")
                    if len(let) == 1 and let.isalpha():
                        break
            #check let in word and increase the value of correct 
            if let in word:
                correct += 1
        #now print the result of player 2
        print("\nYou got ",correct," letters correct\n")
        #ask player to play again 
        choice = input("Would you like to play again? yes/no ")
        if choice == "yes":
            continue
        else:
            break
#call main funtion to start the game 
if __name__ =="__main__":
    main()
