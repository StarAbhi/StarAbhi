def is_valid_username(username):
    digit=letter=0
    #count no of digit and non-digit in username
    for ch in username:
        if ch.isdigit():
            digit =digit+1
        else :
            letter =letter+1
    #condition for correct username
    if len(username)>2 and len(username)<11 and username.isalnum() and username[0].isalpha() and digit <= letter:        
        return True
    else:
        return False

#test case 
print(is_valid_username("Allice123"))
print(is_valid_username("Allic12345"))
print(is_valid_username("2Allice"))
print(is_valid_username("z"))
