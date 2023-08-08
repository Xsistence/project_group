from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    net_profit=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        net_profit.append([row[0],row[1]])   

#print(Cash_on_hand)

def profit_calculation():
    calculated_amount = []
    profit_increasing = True

    for day in range(1, len(net_profit)):
        if int(net_profit[day][1]) < int(net_profit[day - 1][1]):
             profit_increasing = False
             break
        
    if profit_increasing is False:
        for day in range(1, len(net_profit)):
            current_day = int(net_profit[day][1])
            previous_day = int(net_profit[day - 1][1])
            if current_day < previous_day:
                amount = previous_day - current_day
                calculated_amount.append(f'[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount}')

    if profit_increasing is True:
        contended_increment = 0
        chosen_day = 0
        for day in range(1, len(net_profit)):
             current_day = int(net_profit[day][1])
             previous_day = int(net_profit[day - 1][1])
             if contended_increment < current_day - previous_day:
                contended_increment = current_day - previous_day
                chosen_day = day
        calculated_amount = f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n\
[HIGHEST NET PROFIT SURPLUS] DAY: {chosen_day}, AMOUNT: USD{contended_increment}\n'

    return calculated_amount 
        


