# 1st part
def read_file(filename):
    with open(filename, "r") as file:
        lines=file.read().splitlines()
    file.close()
    return lines
#2nd part
def get_words_from_string(line):
    print(list)
    line=line.lower()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ch in line:
        if ch in punctuation:
            line = line.replace(ch, " ")
    words = []
    for word in line.split(" "):
        if word.strip():
            words.append(word)
    return words
#3rd part
def get_words_from_line_list(list_of_lines):
    word_list=[]
    for line in list_of_lines:
        word_list += get_words_from_string(line)
    return word_list
#4th part
def count_frequency(word_list):
    frequency={}
    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
#5th part
def find_most_common_word(freq_map):
    most_common = max(freq_map, key= lambda x: freq_map[x])
    return most_common
#6th part
def write_result(filename):
    lines=read_file(filename)
    words=get_words_from_line_list(lines)
    distinct_words=count_frequency(words)
    most_occuring_words = find_most_common_word(distinct_words)
    file=open("result.txt",'w')
    file.write("File:"+filename+"\n")
    file.write("Number of lines:"+str(len(lines))+"\n")
    file.write("Number of words:"+str(len(words))+"\n")
    file.write("Number of distinct words:"+str(len(distinct_words))+"\n")
    file.write("Most commonly used words:"+most_occuring_words)
    file.close()
#call write_result function 
write_result("test.txt")
