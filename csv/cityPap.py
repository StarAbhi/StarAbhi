import csv
def total_population(filename, cityinfo):
    totalPop=0
    for str3 in cityinfo:
        countryCode = str3[0]
        cityName = str3[1]
        region = str3[2]
        with open (filename, newline='') as f:
            readCsv = csv.reader(f)
            for line in readCsv:
                if (line[0] == countryCode):
                    if (line[1] == cityName):
                        if (line[2] == region):
                            totalPop += int(line[3])
        
    return totalPop
print(total_population("cities.csv",[['py','santa elena','08'],['tz','malangali','04']]))

