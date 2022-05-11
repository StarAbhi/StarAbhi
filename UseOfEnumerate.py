def func(li, antal):

    sum = 0

    for i, e in enumerate(li):

        if i < antal:

            sum += e

    return sum

my_lis = [1,3,2,7,3,14,24,11]

ant = int(input('How many number do u want to add? '))

#new added code
#Here we have to call the function func() 
# by passing my_list and user input number ant
# and store it in sum variable and after this print it 

sum = func(my_lis,ant)
print("Answer : ",sum)

