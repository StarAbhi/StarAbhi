numbers =[10,20,30,40,50]
for num in (elem**2 for elem in numbers if elem%2 == 0):
    print(num,end='')