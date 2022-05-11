import pyinputplus as pyin
def readFile(filename):
    try:
        with open(filename,'r') as file:
            read_file = file.read()
            print(read_file)
        file.close()
    except FileNotFoundError:
        print("File not found !!")
def addNum():
    num=pyin.inputNum("Enter any  number : ")
    file = open("input.txt","a+")
    file.write(str(num)+"\n")
    file.close()

def addLetter():
    while True:
        letter=pyin.inputStr("Enter any alphabetical character : ")
        if letter.isalpha():
            file = open("input.txt","a+")
            file.write(letter)
            file.close()
            break
        else:
            print("Invalid Input!! Try again")
while True:
    print("_______MENU_______")
    print("1.) Read from file")
    print("2.) Add number to file")
    print("3.) Add letter to file")
    print("4.) Quit ")
    choice = pyin.inputChoice(['1','2','3','4'])
    if choice=='1':
        readFile("input.txt")
    elif choice=='2':
        addNum()
    elif choice=='3':
        addLetter()
    elif choice=='4':
        break
    
 