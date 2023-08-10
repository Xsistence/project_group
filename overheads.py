
from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store expense type and amount 
    overheads=[] 

    # append expense type and amount into the overheads list
    for row in reader:
        #get the amount for each expense type
        #and append the overheads list
        overheads.append([row[0],row[1]])   

# create function that returns expense type with the highest amount
def overhead():
    """
    Function returns the expense type with the highest amount 
    based on data stored in overheads list
    """
    # create empty variables to store expense type and its amount for comparison
    highest_overhead = ""
    contended_value = 0
    # for loop to run through overheads list to find expense type with highest amount
    for expense in range(len(overheads)):
        if float(overheads[expense][1]) > float(contended_value):
         contended_value = overheads[expense][1]
         highest_overhead = f"[HIGHEST OVERHEAD] {overheads[expense][0].upper()}: {overheads[expense][1]}%"
    # return expense type with highest amount
    return highest_overhead




