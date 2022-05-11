def is_palindrome(string):
    d = ",.!?/&-:;@'..."
    str=''
    for l in string.lower():
        if l in d :
            string.replace(l,' ')

    return string

print(is_palindrome("str;;ptr"))