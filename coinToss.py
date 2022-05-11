import random
die1=0
die2=0
tie=0
#while loop to  play dice game again and again  
while True:
    play1 = random.randint(1, 6)
    play2 = random.randint(1, 6)
    #condition for Tie
    if play1 == play2:
        tie +=1
        print("Tie!")
    else:
        #check who win 
        if play1>play2:
            die1 +=1
            print("Die1 won!")
        else:
            die2 +=1
            print("Die2 won!")
    #display status of game         
    print("Score Board")
    print("Die1: {} Die2: {} Tie: {}".format(die1,die2,tie))
    #User choice to stop and keep playing 
    choice=input("Would you like to play again? ")
    if choice!='yes':
        break

