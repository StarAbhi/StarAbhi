#assign PI value 
PI=3.14159
#get outer ,inner radius and height input from user in float type 
outerRadius=float(input("Enter the radius of outer surface : "))
innerRadius=float(input("Enter the radius of inner surface : "))
height=float(input("Enter the height of cylinder : "))
#calculate the volume of cylinder ** means power of 
volume=((outerRadius-innerRadius)**2)*height*PI
#print the result 4 decimal place  by f-strings 
print(f'Valume  of hollow cylinder : {volume:.4f}')
