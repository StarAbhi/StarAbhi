import csv
  
# csv file name
filename = "university_records.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, newline='') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
  
    # extracting each data row one by one
    for row in csvreader:
        print(row)