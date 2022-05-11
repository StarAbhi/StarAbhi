import random #it is use for choose random H or T from list 
coin=['H','T'] #list of choice 
ch='y' #this variable use for "play another round?" y/n
tie=0 #it hold the total number of tie 
totalWinP1=0 #it hold the total number of win of player1
totalWinP2=0 #it hold the total number of win of player1
fl=open("instructions.txt") #open  instructions file 
instructions=fl.read() # read all the  instructions data
print(instructions) #print instructions
fl.close() #close file 
while(ch=='y' or ch=='Y'): #while loop for play again according to user choice 
    player1List=[] #list player 1 H and T
    player2List=[] #list player 2 H and T
    player1=0 #count player 1 wins
    player2=0 #count player 2 wins
    p1s=0 #count H H in player 1 
    p2s=0 #count H H in player 2 
    p1p=None #hold previous tosse H or T of player 1
    p2p=None #hold previous tosse H or T of player 2
    count=0 #use to count the number of round when conut=4 loop stop
    while(count!=4):
        choice=input("Heads or Tails?Type H or T > ")#take user choice 
        p1=random.choice(coin) #random value for player1 H or T 
        if p1p==p1=='H':
            p1s +=1
        p1p=p1
        player1List.append(p1) 
        print("Player 1 tossed ",p1) 
        p2=random.choice(coin) #random value for player2 H or T 
        if p2p==p2=='H':
            p2s +=1
        p2p=p2
        player2List.append(p2)
        print("Player 2 tossed ",p2)
        if p1==choice:
            player1 +=1
            print("Player 1 wins")
        if p2==choice:
            player2 +=1
            print("Player 2 wins")
        count +=1
    #print round Stats of both players 
    print("ROUND STATS")
    if player1>player2:
        print("Player 1 wins this round")
        totalWinP1 +=1
    elif player2>player1:
        print("Player 2 wins this round")
        totalWinP2 +=1
    else:
        print("Player 1 and Player 2 Tie this round")
        tie +=1
    print("Player 1 points ",p1)
    print("Player 2 points ",p2)
    print("Player 1 tossed",player1List)
    print("Player 2 tossed",player2List)
    print("H H found in the player 1 sequence ",p1s," times")
    print("H H found in the player 2 sequence ",p2s," times")
    ch=input("Do you want to play another round? y/n >") #user choice to play again or not 
#print summary of game 
print("SUMMARY STATS")
print("Number of ties ",tie )
print("Number of player 1 wins",totalWinP1) 
print("Number of player 2 wins",totalWinP2) 


