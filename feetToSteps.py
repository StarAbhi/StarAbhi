#function for feet to steps 
def feet_to_steps(feet):
    #to convert feet to steps we divide feet by 2.5 and hold
    # the result in steps 
    steps = feet/2.5
    #now return the steps by converting the data type in int 
    return int(steps)

if __name__ == '__main__' :
    #take feet from  user as float value  
    feet = float(input())
    #now call the function and print the result 
    print(feet_to_steps(feet))
