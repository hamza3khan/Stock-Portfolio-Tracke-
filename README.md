Stock Portfolio Tracker (Console Version)

 Project Description

This is a simple **console-based Python application** that tracks stock investments.  
The user enters stock names and how many shares they own, and the program calculates the **total investment** using hardcoded stock prices.



 Features

- Accepts user input for stock symbols and quantities.
- Uses a predefined dictionary of stock prices.
- Calculates the total investment.
- Optionally saves the investment summary to a `.txt` file.



 Technologies Used

- Python (built-in modules only)
  - `input()`, `print()`, `dictionary`, `if-else`, `loops`, `file handling`


 How to Run

1. Make sure Python is installed on your system.
2. Copy the code into a file named `stock_tracker.py`.
3. Run the script:

python stock_tracker.py


Enter stock symbols (like AAPL, TSLA) and quantities.

Type done to finish and see your investment report.

Choose to save the report if you want a .txt file.


 Welcome to the Stock Portfolio Tracker
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

Enter stock symbol: AAPL
Enter quantity of AAPL: 3
Enter stock symbol: TSLA
Enter quantity of TSLA: 2
Enter stock symbol: done
 Investment Summary:
AAPL: 3 shares × $180 = $540
TSLA: 2 shares × $250 = $500
Total Investment: $1040
Do you want to save this report to a text file? (yes/no): yes
 Report saved to 'investment_report.txt'


