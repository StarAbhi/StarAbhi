import csv
def csvToDict(fileName):
    pass
def csvToTuples(fileName):
    list=[]
    with open(fileName, 'r') as myfile:
        for row in csv.reader(myfile):
            if tuple(row) not in list:
                list.append(tuple(row)) 
    print(list)     
fileName=input("Enter file Name :")
csvToDict(fileName)
csvToTuples(fileName)