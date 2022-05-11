import random
#first function generate random temperature in range -10 to 240 as float
# and return the temp 
def generateTemperature():
    temp=random.uniform(-10.0,240.0)
    return temp
#second function to choose your destination until you choose valid enput
# for valid input we make a while infinite loop and ask user to enter decsision
# again and again until user enter corrcect input  
def getDestination():
    while True:
        decsision=input("Where are you going ? ")
        if decsision=="bed" or decsision=="park" or decsision=="space":
            break
        else:
            print("Incorrect choice!! make a correct choice either 'bed' 'park' or 'space' !! ")
    return decsision
#print the temp and destination 
def crazyTemp(value,string):
   print("You find interesting in ",string,"based on the temperature ",value)
#print the menu and use above function to make a trip details 
#in this we use while loop for choose again again for valid choice 
def tripTime():
    temp=None
    destination=None
    while True:
        print("Press the appropriate key for your trip : ")
        print("'1' to get a current temperature : ")
        print("'2' to set your destination ")
        print("'3' get the trip details ")
        print("'Q' to quit ")
        choice=input("Enter Choice : ")
        if choice=="1":
            temp=generateTemperature()
            print("Current Temperature : ",temp)
        elif choice=="2" and temp !=None:
            destination=getDestination()
            print("Corrent Destination : ",destination )
        elif choice=="3" and destination!=None and temp!=None:
            print("Trip Details :- ")
            crazyTemp(temp,destination)
        elif choice=="Q":
            break
        else:
            print("Invalid Choice !! Try Agrain !! ")

#call tripTime to run program
tripTime()
