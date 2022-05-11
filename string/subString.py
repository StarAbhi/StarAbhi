def solution(s):
    d={}
    for i in range(0,len(s)):
        e=i
        for j in range(1,len(s)):
            if(s[i]==s[j]):
                e=j
        if s[i] not in d:
            d[s[i]]=[i,e]
        else:
            if (d[s[i]][1]-d[s[i]][0])<(e-i):
                d[s[i]][0]=i
                d[s[i]][1]=e
    temp=0
    max=None
    for k in d:
        if d[k][1]-d[k][0]>temp:
            max=k
            temp=d[k][1]-d[k][0]
    if max==None:
        result=s[0]
    else:
        result=s[d[max][0]:1+d[max][1]]
    return result

print(solution('cbaabaab'))
print(solution('performance'))
print(solution('cat'))

            


