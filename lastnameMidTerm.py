#Name : 
#Assignment title :
#Assignment due date
#Purpose : Program for calculate and display the projection tuition fee of 5 years 
#give :Tuition fee $26,561.00 ,increase in fee per year is 3%
#let we want to project 5 years from 2021 so assign year = 2021
year=2021
#hold fee in present_fee variable 
present_fee = 26561.00
#increase rate 
increase_in_fee = 3
#next 5 year
projection_years=5
#for loop to print 5 year data one by one 
for i in range(projection_years):
    amount = present_fee
    #change the amount in us dollars by format
    currency = "${:,.2f}". format(amount)
    #print the data 
    print("For Year {} to {} Tuition Fee : {}".format(year,year+1,currency))
    #increase the tuition fee 3%
    present_fee = present_fee*0.03+present_fee
    year +=1
