from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store day and net profit record
    net_profit=[] 

    # append day and net profit record into the net_profit list
    for row in reader:
        # get the net profit for each day
        # and append the net_profit list
        net_profit.append([row[0],row[1]])   

# create function to calculate net profit or profit deficit from net_profit list
def profit_calculation():
    """
    Function returns the days with profit deficit,
    or day with highest profit,
    depending on data in net_profit list
    """

    # create empty list to store calculated day and profit 
    calculated_amount = []

    # create boolean to run calculations for different scenarios
    profit_increasing = True

    # for loop to run through net_profit list to detect if data is to be run through one of two scenarios for calculation
    for day in range(1, len(net_profit)):
        # if loop to check if list has a day where net profit is lower than previous day
        if int(net_profit[day][1]) < int(net_profit[day - 1][1]):
             # set boolean value to false if condition is met to run code through correct calculations
             profit_increasing = False
             break
        
    # if loop to run calculations for fluctuating net profit values
    if profit_increasing is False:
        # for loop to run calculations through entire net_profit list
        for day in range(1, len(net_profit)):
            # create variables to store current and previous day net profit as integer values
            current_day = int(net_profit[day][1])
            previous_day = int(net_profit[day - 1][1])
            # if loop to calculate the days with net profit deficit
            if current_day < previous_day:
                # create variable to store deficit amount
                amount = previous_day - current_day
                # append day and net profit deficit into calculated_amount list
                calculated_amount.append(f'[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount}')

    # if loop to run calculations for always increasing net profit values 
    if profit_increasing is True:
        # create variables to store the highest day and net profit increment
        contended_increment = 0
        chosen_day = 0
        # for loop to run through net_profit list to find day with highest increment
        for day in range(1, len(net_profit)):
             # create variables to store current and previous day net profit as integer values
             current_day = int(net_profit[day][1])
             previous_day = int(net_profit[day - 1][1])
             # if loop to calculate the day with the highest net profit increment
             if contended_increment < current_day - previous_day:
                contended_increment = current_day - previous_day
                chosen_day = day
        # assign to variable the day with the highest net profit increment
        calculated_amount = f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n\
[HIGHEST NET PROFIT SURPLUS] DAY: {chosen_day}, AMOUNT: USD{contended_increment}\n'

    # return the calculated values
    return calculated_amount 
        


