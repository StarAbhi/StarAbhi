def student(fname,lname,grades):
    student_d={'name':fname+" "+lname,'grade':grades}
    print("Student Details in dict Form :- ",student_d)

fname=input("Enter the First Name ")
lname=input("Enter the Last Name ")
grades=eval(input("Enter the Grade "))

student(fname,lname,grades)
