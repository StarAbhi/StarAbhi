from os import remove
import requests
import numpy as np
import pandas as pd

#get the data from API 
r = requests.get('https://coderbyte.com/api/challenges/json/list-numbers')
#store the data in prob 
prob=r.json()['data']
#find the standard deviation of the list numbers 
# by using std() function of numpy and store the value in st_dev1
#also round the value by round() function
st_dev1 = round(np.std(prob))
#for second part we have to remove two max number so use
#max() function to get the max value than remove function to remove 
# the value  two time 
prob.remove(max(prob))
prob.remove(max(prob))
#now again find SD and store in st_dev2 also round the value
st_dev2 = round(np.std(prob))

#print the value
print(st_dev1,st_dev2)
