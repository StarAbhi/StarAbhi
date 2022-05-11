def read_data(filename):
    file = open(filename)
    headers = file.readline().split(',')
    data=list()
    with file as f:
        for line in f:
            data.append(line.split(','))
    #closes the file
    f.close()
    return headers,data


def display_table(headers, data):
    
    print ("{:<8} {:<15} {:<10}".format('Name','Age','Percent'))
    for v in data:
        name, age, perc = v
        print ("{:<8} {:<15} {:<10}".format( name, age, perc))


def get_column(headers, col_name, data):
    pass


headers,data=read_data("university_records.csv")
print(headers,data)
