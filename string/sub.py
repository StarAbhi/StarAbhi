def solution(s):
    diff=0
    st=0
    en=0
    for i in range(0,len(s)):
        e=i
        for j in range(1,len(s)):
            if(s[i]==s[j]):
                e=j
                if diff<(e-i):
                    diff=e-i
                    st=i
                    en=e
    result=s[st:en+1]
    return result

print(solution('cbaabaab'))
print(solution('performance'))
print(solution('cat'))

            


