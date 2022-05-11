def print_e_ending_words(word_list):
    #Traverse all the list word by for loop 
    for word in word_list:
        #check last letter of each word if true print the word  
        if word[-1]=='e' or word[-1]=='E':
            print(word)

#Test function by calling function with list of words 
print("1st Test : ")
print_e_ending_words(['one','two','three','four','five','six','seven','eight','nine','ten'])

print("2nd Test : ")
word_list = ['the','nest','has','five','eggs']
print_e_ending_words(word_list)