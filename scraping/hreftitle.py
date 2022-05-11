from bs4 import BeautifulSoup
import csv  
#take input from user 
file_name=input("Enter input file name : ")
csv_name=input("Enter output file name : ")
#header for csv file  
header = ['Title', 'URL']
#open html file in read mode
file=open(file_name,'r')
data=file.read()
#now BeautifulSoup   data of html file 
soup = BeautifulSoup(data, 'html.parser')
#close the html file 
file.close() 
#use this for store the temp title and url 
titleAndData = []
#now open the csv file in write mode as f and write row in csv file 
with open(csv_name, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    #get all the a tag from html data and take url and text from it 
    for link in soup.find_all('a'):
        titleAndData.append(link.get_text())
        url=link.get('href')
        url=url.lstrip("https://")
        url=url.lstrip("http://")
        url=url.rstrip("/")
        titleAndData.append(url)
        # write the data in csv file 
        writer.writerow(titleAndData)
        titleAndData.clear() 





