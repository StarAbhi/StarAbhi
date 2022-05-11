def main():
    numfile = open("numbers2.csv","r")
    print("Here are the numbers I read from the file 'numbers2.csv' :")
    count = 0
    sum = 0
    for aline in numfile:
        count +=1
        numList = aline.split(",")
        sum += float(numList[0])
        print(float(numList[0]),"then",float(numList[1]))

    numfile.close()
    print("The average of the first number on each line is:",round(sum/count,1))
main() 