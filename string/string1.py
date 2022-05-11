def stats(L):
    #count is use to count ta occrence of letter in a string 
    ques=L.count('?')
    #by using len() we get the Length of string 
    length=len(L)
    #by using split() make a list of word than calculate the length of list by len 
    words=len(L.split(' '))
    #return the info 
    return {'lenght':length,'numbers':words,'question':ques}

#call the function 
print(stats("nothing to see here?"))
print(stats("gooooo????"))
