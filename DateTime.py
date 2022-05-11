#lsit of month
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
#dict of suffixes
suffixes = { 1:"st",2:"nd",3:"rd",0:"th"}
#take input form user 
data=input('''Enter the Date and Time(yyyy-mm-dd hh-mm ) : ''')
#make a list of date and time form user input 
l=data.split(" ")
#make a string d for date 
d=l[0].split("-")
#make a string t for time 
t=l[1].split(":")
#convert time in 12 hour format 
if(int(t[0])>=12):
    if(int(t[0])==12):
        t[0]=str(int(t[0]))
        x="pm"
    else:
        t[0]=str(int(t[0])-12)
        x="pm"
else:
    if(int(t[0])==00):
        t[0]=str(12)
    t[0]=str(int(t[0]))
    x="am"
#join time and add am pm at the end 
time=":".join(t)
time=time+" "+x
#convert month number to Month Name 
which_one = int(d[1])
if 1 <= which_one <= 12:
    d[1]=months[which_one-1]

#Add suffixes by checking last digite of date    
if(int(d[2])==1):
    d[2]=str(int(d[2]))+suffixes[1]
elif(int(d[2])==2):
    d[2]=str(int(d[2]))+suffixes[2]
elif(int(d[2])==3):
    d[2]=str(int(d[2]))+suffixes[3]
else:
    d[2]=str(int(d[2]))+suffixes[0]

y=d[0]
year=d[1]+"'"+y[2:4]
#Output Result  
print(time,"on the",d[2],"of",year)
