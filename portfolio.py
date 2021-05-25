import stock as stk

# startDate = datetime(2015,1,1)
# endDate = datetime(2021,1,1)
# pinterest = Stock("PINS",1)
# prices = pinterest.get_prices(startDate,endDate)
# Stock.get_allocation()
# Stock.get_currentTotalValue()

newStock = ""
while True:
    newStock = input("Please enter a stock ticker symbol: ")
    if newStock.upper() == "DONE":
        break
    quantityOfStock = float(input("Please enter the number of shares you own: "))
    new_stk = stk.Stock(newStock,quantityOfStock)
    print('If you are done entering stocks, please type "Done" and then press enter.')
    
totalValue = stk.Stock.get_currentTotalValue()
allocation = stk.Stock.get_allocation()

print("The total current value of your portfolio is: ",totalValue)
print(allocation["GOOG"])
