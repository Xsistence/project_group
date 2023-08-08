from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    overheads=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        overheads.append([row[0],row[1]])   

def overhead():
    highest_overhead = ""
    contended_value = 0
    for expense in range(len(overheads)):
        if float(overheads[expense][1]) > float(contended_value):
         contended_value = overheads[expense][1]
         highest_overhead = f"[HIGHEST OVERHEAD] {overheads[expense][0].upper()}: {overheads[expense][1]}%"
    return highest_overhead



