# Task #1: Data representation
print("#Task #1: Data representation ")
corpus = '''The quick brown fox jumps over the lazy dog 
        #dog #foxs'''
print(corpus)
words = []
corpus = corpus.replace('\n', "")
words = corpus.split(" ")
print(words)
# Task #2:Data exploration
print("#Task #2:Data exploration")
first_five_items = words[0:5]
print(first_five_items)

# Task #3:Data cleaning
print("#Task #3:Data cleaning ")


def remove_empty(words):
    words_non_empty = []
    for word in words:
        if len(word) > 0:
            words_non_empty.append(word)
    return words_non_empty


words_non_empty = remove_empty(words)
print(words_non_empty)

# Task #4:Data transformation-normalization
print("#Task #4:Data transformation-normalization")


def normalize(words):
    words_normalized = []
    for word in words:
        words_normalized.append(word.lower())
    return words_normalized


words_normalized = normalize(words_non_empty)
print(words_normalized)

# Task #5:Data transformation-hashtag extraction
print("# Task #5:Data transformation-hashtag extraction")


def extract_hashtags(words):
    hashtags = []
    for word in words:
        if word.startswith("#"):
            hashtags.append(word)
    return hashtags


hashtags = extract_hashtags(words_normalized)
print(hashtags)

# Task #6:Hashtag analysis
print("# Task #6:Hashtag analysis")


def count_each_hashtags(hashtags):
    hashtags_dict = {}
    for hashtag in hashtags:
        if hashtag in hashtags_dict:
            hashtags_dict[hashtag] += 1
        else:
            hashtags_dict[hashtag] = 1
    return hashtags_dict


print(count_each_hashtags(hashtags))
