def Find_Repeated(x):
    x2=sorted(x)
    List_Of_Repeated=[]
    for i in x2:
        if x2.count(i)>1:
            List_Of_Repeated.append([i,x2.count(i)])
            for c in range(x2.count(i)):
                for j in x2:
                    if i==j and x2.count(i)>1:
                        x2.remove(i)
    List_Of_Repeated.sort()
    return List_Of_Repeated

List=[1,2,3,4,4,4,5,5,5,5,5,1,1,2,2,3,7,8,6]

# Repeated numbers: [1,2,3,4,5]

# Simple print output:

print(Find_Repeated(List),"\n")

# For a neat output:

print("[ Value , Times Repeated ] \n")
print("For example: [2,4]  The value 2 was repeated 4 times. \n")
for i in Find_Repeated(List):
    print(i)
