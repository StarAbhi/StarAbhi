def bubble(badList):
    length = len(badList) - 1
    unsorted = True

    while unsorted:
        unsorted = False             # this was moved out of the for loop
        for element in range(0,length):
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print (badList)        # comment this out when you're done testing
                unsorted = True      # this was moved up from the else block


# student data example:

student=[{"studentNumber":123456, "firstName":"Jack", "LastName":"Jacob", "Final Grade":79.6},
{"studentNumber":101214, "firstName": "Chris", "LastName": "Henry", "Final Grade":80.0},
{"studentNumber": 145789, "firstName": "Abby", "LastName": "Zainab", "Final Grade":90.5}, 
{"studentNumber":189040, "firstName": "Logan", "LastName":"Aiden", "FinalGrade":60.0}]

print (sorted(student, key = lambda i: (i['firstName'])))
print(student)
 