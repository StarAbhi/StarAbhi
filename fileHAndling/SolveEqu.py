#take file name from user and store it in fileName variable
fileName=input("Enter the name of file ")
#open the file in read mode 
fh = open(fileName,"r")
#read first line of the txt file 
line=fh.readline()
#print the text file first line 
print(line)
#split the equation by = and make a list  
l1=line.split("=")
#in the list at index 0 is variable name and index 1 is equation 
var = l1[0]
#by using eval function solve the equation and store it in solution varibale 
solution=eval(l1[1])
#now print the result .
print(var,"=",solution)
#close the file .
fh.close()
