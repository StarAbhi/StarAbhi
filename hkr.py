#make a function for read file and search word in file 
def readFileAndSearch(word,filename):
    #make a try block to open file if file not found give an error 
    try:
        #open file and read all the data 
        with open(filename,'r') as file:
            read_file_data = file.read()
            #now we make all data in upper case and also word in upper case
            # then we use count method to count the total number of times a 
            # specified word appears in the string.
            num = (read_file_data.upper()).count(word.upper())
            #now print the result 
            print("The word '{}' appears in file '{}' is : {} ".format(word,filename,num))
        #close the file 
        file.close()
    except FileNotFoundError:
        print("File not found !!")
#call the function for test the function
readFileAndSearch('hacker',"hackers.txt")
readFileAndSearch('computer',"hackers.txt")