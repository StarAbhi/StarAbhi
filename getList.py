listOfInt=[]
while True:
    num=int(input())
    if num>0:
        listOfInt.append(num)
    else:
        break
print(min(listOfInt),"and",max(listOfInt))
