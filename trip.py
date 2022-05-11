#this function use to check prime number 
def isprime(c):
    # define a flag variable
    flag = True
    # prime numbers are greater than 1
    if c > 1:
        # check for factors 2 to c
        for i in range(2, c):
            if (c % i) == 0:
                # if factor is found, set flag to True
                flag = False
                # break out of loop
                break
    return flag
#this function display all the valid pythagorean Tripal 
#according to the given condition (a<b<c<n)
#we pass the value of n 
def pythagoreanTripal(n):
    c = 0
    x = 2
    while(c<n):
        for y in range(1 , x +1):
            a = x * x - y * y
            b = 2* x * y
            c= x *x + y * y
            if(c>n):
                break
            if(a==0 or b==0 or c==0):
                break
            if( a < b and b < c and isprime(c)):
                print(a,b,c)
        x = x + 1

pythagoreanTripal(100)