#take user input form user 
string=input("Enter the string ")
string=string.lower()
string = string.replace(" ","")
#make a list form string 
list1=[]
resultDict={1:[],2:[]}
for i in range(0,len(string)):
    if string[i] not in list1:
        list1.append(string[i])
#make seprate groups digite and alphabets
for i in list1:
    if ord(i)>=48 and ord(i)<=57:
        resultDict[1].append(i)
    else:
        resultDict[2].append(i)
#print the resultDict
print(resultDict)