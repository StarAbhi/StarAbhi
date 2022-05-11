#store file name in filename 
filename="airtravel.csv"
#open file and make a list of all lines 
with open(filename,"r") as file:
    lines=file.read().splitlines()
#close file 
file.close()
#count use for count the number of lines
count = 0
sumOf1958 = 0
sumOf1959 = 0
sumOf1960 = 0
#read lines and store the sum of every year
for line in lines:
    count += 1
    data=line.split(",")
    sumOf1958 += int(data[1])
    sumOf1959 += int(data[2])
    sumOf1960 += int(data[3])
#make a dict of year with average passengers 
avg_pass = {"1958":int(sumOf1958/count),"1959":int(sumOf1959/count),"1960":int(sumOf1960/count)}
#print dict as key and value 
print("Average passengers")
for key,value in avg_pass.items():
    print(key," : ",value)