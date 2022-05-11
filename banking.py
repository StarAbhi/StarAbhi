import sys
class Customer:
    bankname="Star Banking"

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance After Deposit : ",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Fund...can't perform this operation ")
            sys.exit()
        self.balance = self.balance-amt
        print("Balance after withdraw : ",self.balance)

print("Welcome to ",Customer.bankname)
name=input("Enter Your Name : ")
c=Customer(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-Exit ")
    option = input("Enter Your Option : ")
    if option == 'd' or option == "D":
        amt = float(input("Enter Amount : "))
        c.deposit(amt)
    elif option == 'w' or option == "W":
        amt=float(input('Enter amount:'))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option..Plz choose valid option')
