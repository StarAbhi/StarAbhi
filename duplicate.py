#function for question 4
def removeDuplicate(list):
    list2=[]
    for i in list:
        if i not in list2:
            list2.append(i)
    
    return list2
#get user input list and call the function and print the result
list = eval(input("Enter the list : "))
print("List : ",list)
print("After removing duplicate :",removeDuplicate(list))

#function for question 5 
def mostFrequent(list):
    result = dict()
    for i in list:
        if i not in result:
            result[i]=1
        else:
            result[i] +=1
    return max(zip(result.values(), result.keys()))[1]
    
#get user input list and call the function and print the result
list2 = eval(input("Enter the list : ")) 
print("List : ",list2)
print("Most Frequent : ",mostFrequent(list2))
