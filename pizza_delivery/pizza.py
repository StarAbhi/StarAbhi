#calculate pizza type price
def cal_type_price(type):
    if type=='cheese':
        return 7
    elif type=='veggle':
        return 5
    elif type=='pepperoni':
        return 9
    elif type=='meat':
        return 12
    elif type=='barbeque chicken':
        return 10
    else:
        print("Invalid Pizza Type : ")
        return 0     
#calculate pizza size price
def cal_size_price(size):
    if size=='small':
        return 2
    elif size=='medium':
        return 5
    elif size=='large':
        return 8
    else:
        print("Invalid Pizza Size ")
        return 0
#calculate pizza topping price
def cal_topping_price(toppings):
    return 1.25*toppings
#calculate pizza dough price
def cal_dough_price(dough):
    if dough=='thin':
        return 5
    elif dough=='thick':
        return 3
    elif dough=='flatbread':
        return 4
    else:
        print("Invalid Dough Type ")
        return 0
#calculate distance price
def cal_distance_price(distance):
    return 1.05*distance
#calculate total tax
def cal_tax_price(total):
    return (total*7.25)/100
#print order details
def print_order_details(order_details):
    print("L-J Pizza Delivery\nYour Order : ")
    for key, value in order_details.items():
        print ("{:<15} ${:<15} ".format( key,"{:.2f}".format( value)))
        if(key=='Miles' or key=='Tax'):
            print()
#main function 
if __name__ == '__main__':
    print("L-J Pizza Delivery\nOrdering Software System")
    order_details={}
    print("Start a new Order ")
    #take order details from user 
    type=input("Enter Pizza Type (Cheese,Veggle,Pepperoni,Meat,Barbeque Chicken)")
    size=input("Enter Pizza Size (Small,Medium,Large)")
    toppings=float(input("Enter Number of Topping "))
    dough=input("Enter Crust(Dough)(Thin,Thick,Flatbread)")
    distance=int(input("Enter Distance in Miles "))
    #calculate price 
    type_price=cal_type_price(type.lower())
    size_price=cal_size_price(size.lower())
    toppings_price=cal_topping_price(toppings)
    dough_price=cal_dough_price(dough.lower())
    distance_price=cal_distance_price(distance)
    total=type_price+size_price+toppings_price+dough_price+distance_price
    tax_price=cal_tax_price(total)
    #make a dict from order data 
    order_details[type.capitalize()]=type_price
    order_details[size.capitalize()]=size_price
    order_details['Toppings']=toppings_price
    order_details[dough.capitalize()]=dough_price
    order_details['Miles']=distance_price
    order_details['Subtotal']=total
    order_details['Tax']=tax_price
    order_details['Total Price']=tax_price+total
    #print order details
    print_order_details(order_details)
        
    

