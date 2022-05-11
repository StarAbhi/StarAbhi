def calculate_pay(payRate,workingHours,bonus):
    total_pay=float(0)
    if workingHours < 8:
        total_pay = workingHours*payRate

    elif workingHours > 8 and workingHours <= 12:
        total_pay = workingHours * payRate + (workingHours - 8) * 1.5 *bonus
    else:
        bonus = bonus + (bonus*0.5)
        total_pay = workingHours*payRate + (workingHours - 12) * 1.5 *bonus
    
    return total_pay

print("calculate_pay(50,4,6) : " ,calculate_pay(50,4,6))
print("calculate_pay(50,9,6) : ",calculate_pay(50,9,6))
print("calculate_pay(50,13,6) : ",calculate_pay(50,13,6))
