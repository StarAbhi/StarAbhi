# while loop use for continue shopping condition 
while True:
    #get user data of item and price 
    item=int(input("How many items "))
    price=int(input("How many price "))
    #make a list for item and price 
    itemList=[]
    itemPrice=[]
    #check if the item and price number same or not
    if item==price:
        #get item and price from the user and add in list 
        for i in range(item):
            item_name=input("Enter item name : ")
            itemList.append(item_name)
            item_price=float(input("Enter item price : "))
            itemPrice.append(item_price)
        #print the both list and total spend price .
        print("List of Item : ",itemList)
        print("List of item Price :",itemPrice)
        print("The total price you spend :",sum(itemPrice))
    else:
        print("The item and price should be same number  ")
    #get user input for continue shopping 
    choice=input("If you want to continue shopping enter 'y' else 'n' for exit : ")
    if(choice=='n'):
        print("Thanks Have a Good day...")
        break


