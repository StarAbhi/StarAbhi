import random

def spin():
    n = random.randint(1,9)
    return(n)
def spin3(count):
    wheel1=spin()
    wheel2=spin()
    wheel3=spin()
    print("Spin Number ",count," : ",wheel1," ",wheel2," ",wheel3)
    result=isWinner(wheel1,wheel2,wheel3)
    return result
def isWinner(wheel1,wheel2,wheel3):
    if(wheel1==wheel2==wheel3):
        return 1
    else :
        return 0
def help():
    print('''    Welcome to your Slot Machine 
    You bet 1 Token for each Spin of the Wheels
    You win 100 Tokens When all Three Wheels are Same
    Good Luck ''')

def start():
    #let User have 100 Token at the start 
    tokens=100
    count=0
    d=input("Enter s to spin ,q to quit , h for help : ")
    while(d=='s' or d=='h'):
        if(d=='s'):
            count +=1
            result=spin3(count)
            if(result==0):
                tokens -= 1
            else:
                tokens += 100
                print("Winner !! You Won 100 Token After ",count," Spins now you have total ",tokens ," Tokens")
                d=input("Enter s to spin ,q to quit , h for help : ")
           
        else:
            help()
            d=input("Enter s to spin ,q to quit , h for help : ")
    print("Thank You for Playing")
        
start()