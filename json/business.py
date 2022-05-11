#import json module to work on json data 
import json
#this part is question 1
zipCode=input("Enter the 5 digit zip code ")
f = open('jsonData.json',)
#by using json.load(open file name ) we load json data 
# load() method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
# It is mainly used for deserializing native string, byte, 
# or byte array which consists of JSON data into Python Dictionary 
data = json.load(f)
#in this section we check zipcode with postal_code if it true we print business data 
print("\n - : Business Info by User given Zip code : - \n")
for business in data:
    if business['postal_code']==zipCode:
        for info in business: 
            print(info,"   :  ",business[info])
        print("\n")

#This part is question no 2
print("\n - : Business who accept Bicton as payment : - \n")
#in this we check Bitcoin Paymenet details avilable or not in business
#if avilable then check if it true then print details of business 
#we also print details in which Bitcoin Paymenet details not avilable
for business in data:
    try:
        if business["attributes"]["BusinessAcceptsBitcoin"]=="True":
            for info in business: 
                print(info,"  :   ",business[info])
    except:
        print("\nBitcoin Paymenet details not avilable in this business ")
        for info in business: 
            print(info,"  :   ",business[info])
f.close()