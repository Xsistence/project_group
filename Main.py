from pathlib import Path

import overheads, cash_on_hand, profit_loss

# create function to write summary report in txt format
def main():
    """
    function returns highest overhead expense, 
    day with highest cash surplus or days with cash deficit,
    day with highest net profit surplus or days with net profit deficit
    based on data from overheads.py, cash_on_hand.py, profit_loss.py
    """
    file_path = Path.cwd()/"Summary_Report.txt"
    file_path.touch()

    # create variable to create correct text format based on whether there was a surplus or deficit
    scenario_check = cash_on_hand.cash_calculation()

    # if loop to write txt file with deficit values in correct format
    if any("DEFICIT" in entry for entry in scenario_check):
        # opening paymentSummary.txt file for exception handling
        with file_path.open(mode = "w", encoding="UTF-8") as file:
            file.write(f'{overheads.overhead()}'"\n")
            for list in cash_on_hand.cash_calculation():
                file.write(str(list) + "\n")
            for list in profit_loss.profit_calculation():
                file.write(str(list) + "\n")

    # else to write txt file with surplus values in correct format
    else: 
        # opening paymentSummary.txt file for exception handling
        with file_path.open(mode = "w", encoding="UTF-8") as file:
            file.write(f'{overheads.overhead()}\n{cash_on_hand.cash_calculation()}\n{profit_loss.profit_calculation()}')

# call main() function to create Summary_Report.txt
main()

