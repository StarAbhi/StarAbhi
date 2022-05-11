def replace_list_element(l,ith,new_element):
    l[ith]=new_element
    return l

my_list=[1,'a',2.1,(2,4,5),{'id':1234}]
l=my_list
ith=3
new_element=[2,4,5]
print(my_list)
my_list=replace_list_element(l,ith,new_element)

print(my_list)