from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store day and cash on hand 
    Cash_on_hand=[] 

    # append day and cash on hand into the cash_on_hand list
    for row in reader:
        #get the day and cash on hand for each record
        #and append the cash_on_hand list
        Cash_on_hand.append([row[0],row[1]])   

# create function cash_calculation to calculate the cash deficit or cash surplus from data stored in cash_on_hand list
def cash_calculation():
    """
    Function returns the days with cash deficit if cash on hand is fluctuating, 
    or day with highest cash surplus if cash on hand is always increasing,
    based on data stored in cash_on_hand list
    """

    # create empty list calculated_amount to store the calculated days and amount
    calculated_amount = []

    # set boolean variable cash_increasing to run correct calculations for different scenarios
    cash_increasing = True

    # for loop to run through cash_on_hand list to detect if data is to be run through one of two scenarios for calculation
    for day in range(1, len(Cash_on_hand)):
        # if loop to check if list contains a day where current day amount is less than previous day
        if int(Cash_on_hand[day][1]) < int(Cash_on_hand[day - 1][1]):
             # set boolean value to False to run data through correct calculations
             cash_increasing = False
             break
        
    # if loop to run calculations for fluctuating cash on hand values
    if cash_increasing is False:
        # for loop to run calcluations through entire cash_on_hand list
        for day in range(1, len(Cash_on_hand)):
            # create variables to store current and previous day cash on hand as integer values
            current_day = int(Cash_on_hand[day][1])
            previous_day = int(Cash_on_hand[day - 1][1])
            # if loop to calculate the days with cash deficit 
            if current_day < previous_day:
                # create variable to store deficit amount 
                amount = previous_day - current_day
                # append day and cash deficit amount into calculated_amount list 
                calculated_amount.append(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}")

    # if loop to run calculations for always increasing cash on hand values
    if cash_increasing is True:
        # create variables to store the data of day with highest increment
        contended_increment = 0
        chosen_day = 0
        # for loop to run through entire cash_on_hand list to find day with highest increment
        for day in range(1, len(Cash_on_hand)):
            # create variables to store current and previous day cash on hand as integer values 
            current_day = int(Cash_on_hand[day][1])
            previous_day = int(Cash_on_hand[day - 1][1])
            # if loop to store new day and increment if higher than previous stored values
            if contended_increment < current_day - previous_day:
                # store the new day with higher increment in chosen_day and cotended_increment variables
                contended_increment = current_day - previous_day
                chosen_day = day
        # store day of highest increment in a string
        calculated_amount = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY \n\
[HIGHEST CASH SURPLUS] DAY: {chosen_day}, AMOUNT: USD{contended_increment}"

    # return the calculated day and amount
    return calculated_amount 
        








        
        
