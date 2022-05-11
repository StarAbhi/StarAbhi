def grocer_item():


    file = open('InputFile.txt', 'r')
    file2 = open('frequency.dat', 'w')
    d = dict()
    for line in file:
        words = line.split(":")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])
       
    file2.close()
    print(d)

#this is my function originally


def grocer_item():


    file = open('InputFile.txt', 'r')
    d = dict()
    for line in file:
        words = line.split(":")
        for word in words:
            word=word.strip()
            if word.isalpha():
                temp=word
            else :
                temp1=word
        d[temp]=temp1    
    for key in list(d.keys()):
        print(key, ":", d[key])
    
grocer_item()
