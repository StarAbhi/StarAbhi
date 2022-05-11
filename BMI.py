#function for calculate BMI
def print_bmi_results(weight,height): 
    #Calculate BMI from height and weight
    BMI=weight/height**2   
    #conditions for BMI
    if BMI<18.5:
        category='Underweight.'
    elif BMI >= 18.5 and BMI<25:
        category='Normal weight.'
    elif BMI >= 25 and BMI<30:
        category='Overweight.'
    else :
        category='Obese.'
    #print the result .
    print("Your BMI category is  : ",category)

#call the function .
print_bmi_results(80,1.8)
print_bmi_results(55.2,1.8)
print_bmi_results(105,1.75)
print_bmi_results(105,2)
