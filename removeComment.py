file1=input("Enter the file name to read : ")
file2=input("Enter the file name to write : ")
f1=open(file1,'r')
lines=f1.readlines()
f2=open(file2,'w')
for line in lines:
    if '#' not in line:
        f2.write(line) 
f1.close()
f2.close()
