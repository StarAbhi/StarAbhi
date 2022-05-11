#CS 177 -project1.py
#{insert your name here}
#summarize the project in a few sentences 

#the definition  of the main function 
def main():
    #print header 
    print('''This program simulates the distance traveled by a tennis ball as it falls within Earth's gravity over time.''')
    #initialize the variables 
    d = 0  
    vt = 0
    a = 9.81
    vi = eval(input("Please enter the initial vertical velocity (meters per secound ): "))
    t  = eval(input("Please enter the time interval (seconds): "))

    #print the header for the output screen
    print("{0:<8}{1:<8}{2:<8}".format("time (s) "," Position (m) "," Velocity (m/s)"))
    
    #use for loop to print the result for every second upto given time interval
    for i in range(t+1):
        #use formulas to determine the value of d and vt 
        d = (vi*i) + (0.5*a*i*i)
        vt = vi + a*i
        #print the result 
        print("{0:<8}{1:>8}{2:>15}".format(i,round(d,2),round(vt,2)))

# calling the main function 
if __name__ == "__main__":
    main()
    