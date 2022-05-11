def load_from_file(filename):
    file=open(filename,'r')
    lines=file.readlines()
    file.close()
    return lines
def location_renking(filename,k):
    file=open(filename,'r')
    data=file.read()
    list=data.split(";")
    dictData={}
    for i in list:
        if i not in dictData:
            dictData[i]=1
        else:
            dictData[i] +=1
    
    
    sort_dictData = sorted(dictData.items(), key=lambda x: x[1], reverse=True)
    result=sort_dictData[0:k:1]
    file.close()
    return result;

def main():
    name=input("Enter the file name : ")
    lines=load_from_file(name)
    print(lines[0])
    print(lines[3])
    print(location_renking(name,3))
    print(location_renking(name,5))
main()

