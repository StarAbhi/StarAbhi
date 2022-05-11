#create dictionary 
my_dict = {'C1':[1,2,3],'C2':[4,5,6],'C3':[7,8,9]}

#iterate  by using for loop 
for key , value in my_dict.items():
    #*value join all list of value by space 
    #print key and value and sum of value  
    print(key,*value,sum(value)) 
