def sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    
    return list
def merge(list1,list2):
    l1=len(list1)
    l2=len(list2)
    if list1[0] < list2[l2-1]:
        list2.extend(list1)
    return list2

list1=eval(input("Enter 1st list "))
list2=eval(input("Enter 2nd list "))

list1=sort(list1)
list2=sort(list2)

print(merge(list1,list2))
print(list1,"\n",list2)