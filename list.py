#The given name list is ..
name=['Brown,Jaylen',
      'Edwards,Carsen',
      'Fall,Tacko\xa0(TW)',
      'Green,Javonte',
      'Langford,Romeo',
      'Nesmith,Aaron',
      'Ojeleye,Semi',
      'Pritchard,Payton',
      'Smart,Marcus',
      'Tatum,Jayson',
      'Teague,Jeff',
      'Theis,Daniel',
      'Thompson,Tristan',
      'Walker,Kemba',
      'Waters,Tremont\xa0(TW)',
      'Williams,Grant',
      'Williams,Robert']
temp=[] #temp[]  list use to hold the temporary list to split first name and last name 
fname=[] #fname[] list use to hold the first name 
lname=[] #lname[] list use to hold the last name 
for i in name:      #we use for loop to take all name one by one 
    temp=i.split(",")   #then we use split function to split the name and hold it in temp list
    fname.append(temp[0])  #we append first name in fname list 
    lname.append(temp[1])  #we append last name in lname list 
    temp.clear()    #At last we clear temp list 
print("Given Name list :-")
print(name)
print("First Name list :-")
print(fname)
print("Last Name list :-")
print(lname)