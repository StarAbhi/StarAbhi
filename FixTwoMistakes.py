num = int(input('Please enter a number to evaluate:'))
if num == 0:
    print("You have entered Zero!")
elif num % 2 == 0:
    print('The {num} is an EVEN number!'.format(num=num))
else:
    print('The {num} is an Odd number!'.format(num=num))
