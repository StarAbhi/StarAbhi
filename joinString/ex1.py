#define words
words = ['A panda eats',' shoots',' and leaves.']
#create function for commas
def with_commas(words):
    result = ','.join(words)
    return result
#create function for spaces
def with_spaces(words):
    result = ' '.join(words)
    return result

#test by calling both function.. 
print(with_commas(words))
print(with_spaces(words))
