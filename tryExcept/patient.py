import ast
def patientData():
    count=0
    while(count!=3):
        try:
            count +=1
            password=input("Please Enter the Password : ")
            if (password=='password'):
                patient=open('data.txt')
                info=ast.literal_eval(patient.readline())
                print("First Name :",info['First'],"\nMiddle Name :",info['Middle'])
                print("Last Name :",info['Last'],"\nSS :",info['SS'])
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect Password !! Try Again  ")
            print("You have ",3-count," Attempts Remaining ")
            continue
    
patientData()
