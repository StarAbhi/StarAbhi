#take input from user 
inputStr=input("Enter the string :- ")
#make a list of symbol you want to remove 
list1=[",","'",";",".","!"]
#remove  symbol from string 
for i in list1:
        inputStr=inputStr.replace(i,"")
#split the string and make a list of words 
list2=inputStr.split(" ")
#remove space from list 
for i in list2:
    if i == '':
        list2.remove(i)
#now sort the list 
list2.sort()
dict1={}
#make a dict of words and it's frequency
for i in list2:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else :
        dict1[i]=1
#now print the dict .
for i in dict1:
    print(i+":"+str(dict1[i]))
