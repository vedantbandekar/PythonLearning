#Writing csv file in python(comma separated values)

import json
import csv

employees = [["Name", "Age", "Job"],
             ["Mark", 31, "Director"],
             ["Jack", 27, "Youtuber"],
             ["Pewdiepie", 35, "Retired"]]

file_path = "output.csv"

with open(file_path, "w", newline="") as file: #There adding keywrod arg of new line blank to avoid it
    writer = csv.writer(file) #csv file will be created but need to iterate list
    for row in employees:
        writer.writerow(row) #This gives new line after every list insidde list
    print(f"CSV file '{file_path}' was created")
