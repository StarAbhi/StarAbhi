def ConVow(file):
    fileHandle = open(file, "r")
    con = 0
    vow = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in fileHandle.read():
        if char>='a' and char<='z':
            if char not in vowels:
                con +=1
            else:
                vow +=1
        elif char>='A' and char<='Z':
            if char not in vowels:
                con +=1
            else:
                vow +=1
    fileHandle.close()
    print("Total Consonants : ",con,"\nTotal Vowels : ",vow)
def words(file):
    fileHandle = open(file,"r")
    data = fileHandle.read()
    words = data.split()
    count = 0
    for word in words:
        if len(word)<5:
            count +=1
    print("Number of word less than 5 length : ",count)
def palin(file):
    fileHandle = open(file,"r")
    data = fileHandle.read()
    words = data.split()
    count = 0
    for word in words:
        if  word == word[::-1]:
            count +=1
    print("Number of Palindrome : ",count)
file ="sample.txt"
ConVow(file)
words(file)
palin(file)
