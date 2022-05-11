s=''
strList=[]
while(True):
    s=input()
    if s!='Q':
        strList.append(s)
    else:
        break

strTuple=tuple(x.upper()[::-1] for x in strList)
print(strTuple)