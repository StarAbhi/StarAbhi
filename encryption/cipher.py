def caesar_cipher():
    message=input("your message? ")
    encodingkey = int(input("Encoding key? "))
    cipher=""
    for i in message.upper():
        if i==' ':
            cipher +=' '
        else:
            cipher +=chr((ord(i) + encodingkey-65) % 26 + 65)
    return cipher

caesar_cipher()