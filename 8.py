def word_count(text):
    return len( text.split(" ") )

msu_wiki ="Montclair State University (MSU) is a public research university."
print(word_count(msu_wiki))