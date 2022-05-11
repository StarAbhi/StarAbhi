def compare(list1, list2):
    result=[]
    for i in range(len(list1)):
        if list1[i] >list2[i]:
            result.append(list1[i])
        else:
            result.append(list2[i])
    return result
list1=[5,3,-4,6,10]
list2=[4,4,9,6,4]
larger=compare(list1,list2)
print(" List1 : ",list1,"\n","List2 : ",list2,"\n","Larger : ",larger)
print("So the Sum is ",sum(larger))