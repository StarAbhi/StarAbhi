#for this question we have take a string and make a 
#new string form it the new string contain only unique 
#unique letters than subtract the orignal string len from 
#new string length so we get the minimum number of deletions 
def getMinDeletions(s):
    #define a new string 
    str=''
    #create a new str 
    for ch in s:
        if ch not in str:
            str += ch
    #get the number of deletions required 
    deletion = len(s)-len(str)
    #return the value of deletion 
    return deletion

if __name__ == '__main__':
    #test the function  
    print("abab  : ",getMinDeletions("abab"))
    print("abcab  : ",getMinDeletions("abcab"))

