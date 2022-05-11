fname=input("Please Enter your first name : ")
mname=input("Please Enter your capitalized middle initial  : ")
lname=input("Please Enter your last name : ")
result=fname+" "+mname+" "+lname;
out1=fname[0].lower()+fname[1::].upper()+" "+mname.lower()+" "+lname[0].lower()+lname[1::].upper()
out2=result.lower()
out3=result.upper()
out4=result.capitalize()
out5=fname.capitalize()+" "+mname.capitalize()+" "+lname.capitalize()

print("Concatenated Fullname = ",result)
print(out1,"\n",out2,"\n",out3,"\n",out4,"\n",out5,"\n")
