def setOfBigIntegers(listOfInt):
    if len(listOfInt)==0:
        print(listOfInt)
        return []
    else:
        print(listOfInt[1:])
        return [listOfInt[0]] if abs(listOfInt[0]) > 20 else [] + setOfBigIntegers(listOfInt[1:])


print(setOfBigIntegers([38,5,10,-11,20,49,-19,38,-11,29,0,-28]))