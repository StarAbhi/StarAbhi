#calculate carpet cost by length  width and price of carpet
def carpet_cost(length,width,price):
    area_in_sqr_yard=(length*width)/9
    return area_in_sqr_yard*price

#calculate stitching cost for per line foot
def stitching_cost(length,width,stitching_price):
    total_liner_feet=2*(length+width)
    return total_liner_feet*stitching_price

#calculate sales tax for total cost by 7.5%
def cal_sales_tax(total_cost):
    tax = total_cost*0.075
    return tax

#main function 
if __name__ == '__main__':
    #get data from user 
    price=float(input("Enter the cost of carpet per square yard : "))
    length=float(input("Enter the length of the carpet (in feet) : "))
    width=float(input("Enter the width of the carpet (in feet) :"))
    stitching_price=float(input("Enter the stitching fee per linear foot : "))
    #call function and calculate cost 
    carpet_price=carpet_cost(length,width,price)
    carpet_stitching_price=stitching_cost(length,width,stitching_price)
    total_cost = float(carpet_price+carpet_stitching_price)
    sales_tax=cal_sales_tax(total_cost)
    final_cost=sales_tax+total_cost
    #display the result to 2 decimal places
    print("The cost of the carpet = ","{:.2f}".format(carpet_price))
    print("The stitching fee = ","{:.2f}".format(carpet_stitching_price))
    print("Sales tax = ","{:.2f}".format(sales_tax))
    print("Amount due = ","{:.2f}".format(final_cost))
