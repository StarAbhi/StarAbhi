import random
import math
'''find prime'''
def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
        else:
            return True

'''Finding ending score'''
def rollUnitll():
    score=100
    Rolls= []
    count=0
    while True:
        dicenum= random.randint(1,6)
        if prime(dicenum):
            count +=1
        if count==3:
            break
  
        else:
            Rolls.append(dicenum)
            score -=5
    #add average maximum and minimum and find it's value 
    average=sum(Rolls)/len(Rolls)
    minimum=min(Rolls)
    maximum=max(Rolls)
    #return all the values 
    return Rolls,score,average,maximum,minimum


print('Q1')
print('Sample runs:')
for i in range (5):
    rolls,score,average,minimum,maximum=rollUnitll()
    print('Rolls made:',rolls)
    print('Average :',average)
    print('Maximum :',maximum)
    print('Minimum :',minimum)
    print('Ending score is:',score)
    print()
    