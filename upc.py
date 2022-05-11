#define a function to check UPC number
def is_valid_upc(list_of_integers):
    #define result to store the sum of digits
    result=0
    # get the lenght of list
    digits=len(list_of_integers)
    #chaeck condition for valid and return True or False 
    if digits>2 and sum(list_of_integers)>0:
        for i in range(digits-1,0,-1):
            if i%2==0:
                result +=list_of_integers[i]*3
            else:
                result +=list_of_integers[i]
        if result%10==0:
            return True
        else:
            return False
    else:
        return False
#get the list input from user 
list_of_integers = eval(input("Enter the UPC number : "))
#call the function and print the result 
print(is_valid_upc(list_of_integers))
