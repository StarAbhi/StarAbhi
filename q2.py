#question2
def qualInts(From,To):
    L=[]
    for n in range(From,To+1):
        if ( ( n%9==0) or (n %13==0)) and (n %5==0):
            L.append(n)
    return L

def sum(L):
    s=0
    for i in L:
        s=s+i
    return s
print('Q2')
L=qualInts(50,150)
print('List :',L)
print('Sum of List : ',sum(L))
print()