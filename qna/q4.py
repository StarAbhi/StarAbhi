# map() function returns a map object(which is an iterator) of 
# the results after applying the given 
# function to each item of a given iterable (list, tuple etc.)
#for Ex: -

# Return mul of n
def mul(num):
    return num * num
  
# We do num*num all list numbers using map()
numbers = (1, 2, 3, 4)
numbers2 = map(mul, numbers)
print(list(numbers2))

