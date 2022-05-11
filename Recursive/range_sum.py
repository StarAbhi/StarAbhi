def range_sum(n,m):
    #check condition if n>m return 0
    if n > m:
        return 0
    #check n<m
    if n < m:
        return n+range_sum(n+1,m)
    else:
        return  m

#test case 1
print(range_sum(10,4))
#test case 2
print(range_sum(4,10))