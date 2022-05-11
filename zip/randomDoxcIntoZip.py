import zipfile
import random
#this function use for generate 10 random docx file with random words 
def generate_doxc_file(filename,linecount):
    #we define some noun verb adjective and adverb for writing text into .docx file 
    nouns = ("Albert Einstein", "The president", "Disneyland", "Freedom", "Basketball")
    verbs = ("run","dance","slide","jump","think","stand")
    adjectives = ( "enormous.", "doglike.", "silly.", "yellow.", "fun.", "fast.")
    adverb = ("abruptly", " beautifully", " wearily", "quickly", "firmly")
    
    sentence = [nouns, verbs, adverb, adjectives]
    #make write random words in docx file
    with open(filename,'w') as f:
        for i in range(linecount):
            f.writelines([' '.join([random.choice(i) for i in sentence]),'\n'])


## make a zip file for 10 docx file

def convert_doxc_to_zip():

    name_of_Zipfile = 'Doxc_zip_file.zip'

    # opening the 'Zip file' in writing mode by 'a'
    with zipfile.ZipFile(name_of_Zipfile, 'a') as zip_file:
        # append mode adds files to the 'Zip'
        # you have to create the files which you have to add to the 'Zip'
        for i in range(1,11,1):
            zip_file.write("file"+str(i)+".doxc")
            
        print('Files added to the Zip')

    # opening the 'Zip' in reading mode to print all file name 
    with zipfile.ZipFile(name_of_Zipfile, 'r') as file:
        print(zip_file.namelist())



if __name__ == '__main__':
    #make 10 doxc with some random text of size 100 - 150 
    for i in range(1,11,1):
        generate_doxc_file("file"+str(i)+".doxc",35)
    #call convert_doxc_to_zip function to make zip file from doxc file  
    convert_doxc_to_zip()
    