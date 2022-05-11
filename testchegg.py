word = input("Type a word : ")
randomizer = input("Type a number: ")
lucky = int(randomizer) * len(word)
lucky -= 4
randomizer = lucky // 7
print( "your lucky number is", lucky % 100)
