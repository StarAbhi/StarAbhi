
def addHobby():
    f=open("hobby.txt",'w') 
    info=input("Enter Your Hobby  ")
    f.write(info)
    f.close() 
    print("\n")

def readFile():
    f=open("hobby.txt","r")
    list=f.readlines()
    for i in list:
        print(i,end="")
    f.close()
    print("\n")

def countWords():
    count=0
    f=open("hobby.txt","r")
    list=f.readlines()
    words=list[0].split(".")
    for i in words:
        count +=len(i.split())
    f.close()
    print("\nTotal words in txt file ",count)
    print("\n")

def addAmbition():
    f=open("hobby.txt",'a')
    amb=input("\nEnter Your Ambition ")
    f.write(amb)
    f.close()
    print("\n")

def read100char():
    f=open("hobby.txt","r")
    char100=f.read(100)
    print(char100)
    print("\n")

def display():
    count=0;
    f=open("hobby.txt","r")
    list=f.readlines()
    for i in list[0]:
        print(i,end="")
        if count==10:
            print("#",end="")
            count=0
        count +=1
    print("\n")

def read11Toend():
    f=open("hobby.txt","r")
    f.seek(11)
    list=f.readlines()
    for i in list:
        print(i,end="")
    f.close()
    print("\n")

def addSrt():
    f=open("hobby.txt","r")
    list=f.readlines()
    add=list[0].split(".")
    for i in add:
        print(i+" ^_^",end="")
    f.close()
    print("\n")

print("Add Hobby \n")
addHobby()
print("1. Read the file and display all content of the 'hobby.txt' file.  \n")
readFile()
print("2. Count how many words inside the text file you have created.\n ")
countWords()
print("3. Write about your ambition and save it in the same file without losing the previously written content. \n")
addAmbition()
print("4. Print only the first 100 characters inside the file \n")
read100char()
print("5. Display '#' after each and every 10 character \n")
display()
print("6. Read the file content starting from the 11th character until the end \n")
read11Toend()
print("Add the string '^_^' at every end of the line\n")
addSrt()