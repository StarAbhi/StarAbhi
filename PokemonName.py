import random as ran
first=str(input("Enter the first word : "))
second=str(input("Enter the second word : "))
l1=len(first)//2
l2=len(second)//2
index_start1=ran.randint(2,l1)
index_start2=ran.randint(2,l2)
length_substring1=ran.randint(2,l1)
length_substring2=ran.randint(2,l2)
s1=first[index_start1:index_start1+length_substring1]
s2=second[index_start2:index_start2+length_substring1]
result='Your pokemon name is '+(s1+s2).capitalize()
print("**"+"*"*len(result)+"**")
print("* "+" "*len(result)+" *")
print("* "+result+" *")
print("* "+" "*len(result)+" *")
print("**"+"*"*len(result)+"**")