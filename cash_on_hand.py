from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    Cash_on_hand=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        Cash_on_hand.append([row[0],row[1]])   

def cash_calculation():
    calculated_amount = []
    cash_increasing = True

    for day in range(1, len(Cash_on_hand)):
        if int(Cash_on_hand[day][1]) < int(Cash_on_hand[day - 1][1]):
             cash_increasing = False
             break
        
    if cash_increasing is False:
        for day in range(1, len(Cash_on_hand)):
            current_day = int(Cash_on_hand[day][1])
            previous_day = int(Cash_on_hand[day - 1][1])
            if current_day < previous_day:
                amount = previous_day - current_day
                calculated_amount.append(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}")

    if cash_increasing is True:
        contended_increment = 0
        chosen_day = 0
        for day in range(1, len(Cash_on_hand)):
             current_day = int(Cash_on_hand[day][1])
             previous_day = int(Cash_on_hand[day - 1][1])
             if contended_increment < current_day - previous_day:
                contended_increment = current_day - previous_day
                chosen_day = day
        calculated_amount = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY \n\
[HIGHEST CASH SURPLUS] DAY: {chosen_day}, AMOUNT: USD{contended_increment}"

    return calculated_amount 
        








        
        
