def add_to_cart(name,quantity,cart,items,):
    flag = False
    for item in items:
        list=item.split(",")
        if list[0].lower()==name.lower():
            flag = True
    return flag 
        
    
def checkout(cart):
    total = 0
    for item_info in cart:
        total += item_info[1]*item_info[2]
        item_info=[str(i) for i in item_info]
        print(",".join(item_info))  
    return total

def main():
    items = ['AX Jacket,202.99','RL Polo,60.99','AK Tops,19.99','Levis Jeans,65.78']
    cart = []

    print('Welcome to shopping at Amazing209!\n')
    user_input = ''
    while user_input!='quit':
        print("1. Purchase clothes\n2. Checkout")
        user_input=input("Please input an option or type 'quit' exit the program: ")
        if(user_input=="1"):
            print("List of available items")
            print("-----------------------")
            for item in items:
                print(item)
            name = input("Enter the item name to purchase: ")
            quantity = int(input("Enter the quantity: "))
            if add_to_cart(name,quantity,cart,items):
                for item in items:
                    list=item.split(",")
                    if list[0].lower()==name.lower():
                        cart.append([list[0],float(list[1]),quantity])
                        print("{} {} added to your cart".format(quantity,name))
            else:
                print("Name not matched in items list !!")
        elif user_input =='2':
            print("The total amount is: $",checkout(cart))

        else:
            pass
main()
