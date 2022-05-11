import pps_emu  # Physical Programming Simulator
import time     # To apply delay

# menu of the restaurant
menu = [
    ['Mojito', 10.99],
    ['Blue Lagoon', 8.99],
    ['Beer', 12.99],
    ['Sandwich', 14.99],
    ['Cheese Burger', 14.99],
    ['Cheese Fries', 4.99],
    ['Pizza', 18.99],
    ['Hamburger', 10.99],
    ['Hot dog', 4.99],
    ['Ice cream', 11.99]]

# list of orders
order = []


# function to print menu
def printMenu(menu):
    print('Please choose the item [No] you want to add to your order:')
    # print header
    print(f"\n{'No.' : <5}{'Item' : <15} {'Price'}")
    # iterate and print each item in menu
    for i in range(0, len(menu)):
       print(f"{(i + 1) : <5}{menu[i][0] : <15} ${menu[i][1] : <8}")
    print('\nPress -1 to exit\n')




# function to add item to menu
def addItem(menu, order):
    # get item no from user
    while True:          #This is what I added to handle the error if user enters a string but now im having trouble exiting using -1 value
        try:
            itemNo = int(input('your choice :'))
            break
        except ValueError:
            print("Please input integer only...")
            continue

        # get item no from user
        itemNo = int(input('your choice : '))
        # validate item no
        if itemNo == -1:
            return itemNo
        while itemNo not in range(1, len(menu) + 1):
            itemNo = int(input('Invalid input, try again: '))
            if itemNo == -1:
                return itemNo

    # get quantity from user
    quantity = int(input('Enter order quantity: '))

    # if item is already in order list, change quantity, otherwise add fresh item
    if itemNo in [row[0] for row in order]:
        order[[row[0] for row in order].index(itemNo)][3] = order[[row[0] for row in order].index(itemNo)][3] + quantity
    else:
        order.append([itemNo, menu[itemNo - 1][0], menu[itemNo - 1][1], quantity])

    # print which item is added with quantity
    print(quantity, menu[itemNo - 1][0], 'added\n')
    return itemNo


# print order list
def printOrder(order):
    sensor = pps_emu.Sensor()  # This allows us to use the controls and get info for the physical programming simulator

    total = 0

    print('\n*************')
    print('Order slip:')
    print('*************\n')

    # print header
    print(f"{'No.' : <5}{'Item' : <15}{'Qty' : <8}{'Price' : <10}{'Total' : <8}")
    # iterate and print each item in order list and calculate Total
    for i in range(0, len(order)):
        print(
            f"{(i + 1) : <5}{order[i][1] : <15}{order[i][3] : <8}{'${:.2f}'.format(order[i][2]) : <10}{'${:.2f}'.format(order[i][2] * order[i][3]) : <8}")
        total = total + order[i][2] * order[i][3]
    print() # A blank line for aesthetics
    # print total
    print(f"{'Total Bill : ' : <38}${'{:.2f}'.format(total) : <8}")
    print()  # A blank line for aesthetics
    print('Thank you for your purchase')
    print('Your order is in progress.......')


    while True:
        for i in ['rled']:
            for j in range(0, 15,):  # Flash Red LED 15 times
                sensor.output(i, 'on')
                time.sleep(.25)
                sensor.output(i, 'off')
                time.sleep(.25)
        break


# print header
print('*******************************')
print('Welcome to Sunshine Restaurant')
print('********************************')
print()

# while user wants to add more items
while (True):
    # print menu
    printMenu(menu)
    # add item
    val = addItem(menu, order)
    # break loop if user wants to quit
    if (val == -1):
      print('You did not choose an order [No]')
      print('Please let us know if you need assistance')
      print('__________________________________________')
      print()
    else:
        break
while (True):
    # print menu
    printMenu(menu)
    # add item
    val = addItem(menu, order)
    if (val == -1):

# print order
      printOrder(order)
