#get file object reference to the file
file = open("tech.txt", "r")
#read all content of file and make a  data list
data = file.readlines()
#in data list we get all the file text line so we have to combine all the line by using join() we join all line . 
data=(" ").join(data)
#After this we have to remove all (.) so we use split()
info=data.split(".")
#then join() again by join()
info=(" ").join(info)
#then we remove all the (,) by split()
info=info.split(",")
#now again join()
info=(" ").join(info)
#by using replace() we have to remove extra space
info=info.replace('  ','')
#Now we make a list of words[] and get all the info string in word 
words=info.split(" ")

#Make a empty dictinory and get all the the word as key and the occurrences as value by using for loop 
counts={}
for word in words:
    if word in counts:
            counts[word] += 1
    else:
        counts[word] = 1
#now we get max value and key from dict by using max()
n=max(counts,key=counts.get)
print(n," : ",counts[n])
