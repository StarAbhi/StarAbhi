DB = dict()
DB['Student1'] = ['Ahmed',20]
DB['Student2'] = ['Yasser',21]
print(DB.keys())
print(DB.values())
for key,value in DB.items():
    print(key,value)

print(DB['Student2'])

DB['Student2'] = ['Turki',22]
print(DB['Student2'])