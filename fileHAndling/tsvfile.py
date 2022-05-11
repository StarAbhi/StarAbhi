import csv
def load_friendsdb(file_name):
    friends_list=[]
    info={'name':'','height':0}
    with open(file_name) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            info['name']=line[0]
            info['height']=int(line[1])
            friends_list.append(info)
    return friends_list

print(load_friendsdb("friendsdb.tsv"))
