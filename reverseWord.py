#get input from user start index end index and word 
start=int(input("Enter the start index : "))
end=int(input("Enter the end index : "))
word=input("Enter the word : ")
#Now break the given word into three part first mid and last by using string slicing 
#Now slice fist 
first=word[0:start:1]
#slice mid and also reverse the mid 
mid=word[end:start-1:-1]
#slice last 
last=word[end+1::1]
#At the end add all three and print the result 
result=first+mid+last
print(result)
