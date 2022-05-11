import itertools
#itertools.product() is used to find the cartesian product from 
#the given iterator, output is lexicographic ordered.
def coin(n):
  allComb=list(itertools.product("HT", repeat=n))
  result =[''.join(temp) for temp in allComb]
  return result

print(coin(1))
print(coin(2))
print(coin(3))
