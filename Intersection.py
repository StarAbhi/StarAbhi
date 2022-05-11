l1=eval(input("Enter First list"))
l2=eval(input("Enter Secound list"))
inter=[]
if(len(l1)>len(l2)):
    for i in l2:
        if i in l1:
            if i not in inter:
                inter.append(i)
else:
    for i in l1:
        if i in l2:
            if i not in inter:
                inter.append(i)
        

print(l1, " intersection  ",l2 ," is ",inter)