def write_phonebook(phonebook):
    f = open('phonebook.txt','w')
    for name in phonebook:
        number = phonebook[name]
        #BLANK
        f.write(name+","+number+"\n")

write_phonebook({"Abhi":"7379790988","Ashu":"9839986102"})