def midCircular(cir,start,size):
    l=len(cir)
    tempArray=[None]*size
    ind=start-l
    j=0
    for i in range(ind,ind+size,1):
        tempArray[j]=cir[i]
        j+=1
    for i in range(j):
        for k in range(j):
            if tempArray[i]<tempArray[k]:
                temp=tempArray[i]
                tempArray[i]=tempArray[k]
                tempArray[k]=temp
    smin=tempArray[1]
    smax=tempArray[-2]
    for i in range(len(cir)):
        if cir[i]==smax:
            cir[i-1]=smax+smin
        elif cir[i]==smin:
            cir[i+1]=smax*smin
    print("Second Maximum = ",smax)
    print("Second Minimum = ",smin)
    print(cir)

cir1 = [44,59,0,0,0,0,21,11,13,4] 
start1 = 6
size1 = 6
midCircular(cir1,start1,size1)
print("\n")
cir2 = [1,-2,-6,0,5,6,7,10]
start2 = 4
size2 = 7
midCircular(cir2,start2,size2)
