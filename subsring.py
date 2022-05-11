# make a test_str variable for storing string 
test_str = input("Enter the string : ")
  
  
# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
  
# make set of all the substring that have same first and last character
substr=set()
for i in res:
    if i[0] == i[-1]:
        substr.add(i)

# printing result set of all subsring  
print("There are ",len(substr)+1, " substrings with the same first and last character ")