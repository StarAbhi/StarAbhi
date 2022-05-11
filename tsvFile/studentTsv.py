from typing import TypeVar


import csv
with open("StudentInfo.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        print(row[0].split("  "))
