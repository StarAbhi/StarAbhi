from random import randrange
def get_word_of_the_day(day):
    #open words text file 
    file = open("words.txt")
    #read all the data from text file and split it and store it in data 
    data = file.read().split()
    #convert day into corresponding letter
    if(day<=26):
        letter=chr(96+day)
    else:
        letter=chr (96+(day%26))
    
    found = []
    for m in data:
        if m.startswith(letter): #It will check if the input value match with from begining of the signl world
                found.append(m) # Store the value if match

    i = randrange(len(found))
    wordOfDay = found[i]
    return wordOfDay


if __name__ == '__main__':
    print(get_word_of_the_day(27))