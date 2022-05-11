pennies=int(input("How many pennies do you have ? "))
dollar,quarter,dime,nickel=0,0,0,0
if pennies>=5:
    if pennies>100:
        dollar=pennies//100
        pennies=pennies-dollar*100
    if pennies>25:
        quarter=pennies//25
        pennies=pennies-quarter*25
    if pennies>10:
        dime=pennies//10
        pennies=pennies-dime*10
    if pennies>5:
        nickel=pennies//5
        pennies=pennies-nickel*5
    print("{} dollar(s); {} quarter(s); {} dime(s);".format(dollar,quarter,dime),end='') 
    print("{} nickel(s); and {} pennies (left over).".format(nickel,pennies))
else:
    if pennies<0:
        print("It's not possible to have negative pennies!")
    else:
        print("Sorry, 5 pennies is the minimum!")





