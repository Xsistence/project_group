from pathlib import Path

import overheads, cash_on_hand, profit_loss

def main():
    file_path = Path.cwd()/"Summary_Report.txt"
    file_path.touch()
    scenario_check = cash_on_hand.cash_calculation()
    if any("DEFICIT" in entry for entry in scenario_check):
        with file_path.open(mode = "w") as file:
            file.write(f'{overheads.overhead()}'"\n")
            for list in cash_on_hand.cash_calculation():
                file.write(str(list) + "\n")
            for list in profit_loss.profit_calculation():
                file.write(str(list) + "\n")

    else: 
        with file_path.open(mode = "w") as file:
            file.write(f'{overheads.overhead()}\n{cash_on_hand.cash_calculation()}\n{profit_loss.profit_calculation()}')
main()

#Sean Chua 