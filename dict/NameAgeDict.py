#Create a dictionary with a name (String) as the key and an age (Integer)
#as the value. Fill the dictionary by reading the values in
#from a text file (Lab5B1.txt). Each line in the text file
#will have a name and an age.
diction5B1 = {}
file = open("Lab5B1.txt", 'r')
for line in file:
    line = line.strip()
    list = line.split()
    names = list[0]
    ages = int(list[1])
    diction5B1[names] = ages
print("My Dictionary:",diction5B1)
print()

#Ask the user to enter a name and determine if that name is in the map.
#Print a statement to say if it is or not.
nameInDictionary = input("Enter a name: ")
if nameInDictionary in diction5B1.keys():
    print("This name is in the dictionary.")
  
else:
    print("This name is not in the dictionary, please enter a new name.")

# I receive this error statement: " valueList = list(diction5B1.values())
#TypeError: 'list' object is not callable"

valueList = [ v for k , v in diction5B1.items()]
#Ask the user for an age and count how many times
#that age appears in the map. Print the count with a label.
userAge = int(input("\nEnter an age: "))
count = valueList.count(userAge)
print("The age you entered is found",count,"times.")

#after the code above how would I read the list and find the highest age in the group?       

#Read through the values and calculate the highest age in the group
maxAge=max(valueList)
print("The highest age in the group is",maxAge)
