import random
def random_L():
    #by using random module  
    # We Randomly generate a ascii value
    # from  'A' to 'Z' than convert ascii value into character
    return chr(random.randint(ord('A'), ord('Z')))

#call the function 
print(random_L())
