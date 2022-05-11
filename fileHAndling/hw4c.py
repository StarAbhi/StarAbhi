file=open("hw4c.txt",'r')
lines=file.readlines()
for line in lines:
    print(line)
file.close()
name=input("Enter your name : ")
file=open('hw3c_guest.txt','w')
file.write(name)
file.close()