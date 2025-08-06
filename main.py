
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 300,
    "AMZN": 3400
}

portfolio = {}
total_investment = 0

print(" Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' to finish.\n")


while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(" Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print(" Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity


print("\n Investment Summary:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\n Total Investment: ${total_investment}")


save = input("Do you want to save this report to a text file? (yes/no): ").lower()
if save == "yes":
    with open("investment_report.txt", "w") as file:
        file.write("Investment Summary:\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print(" Report saved to 'investment_report.txt'")
