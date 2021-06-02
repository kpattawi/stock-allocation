import pandas as pd

import stock as stk


# # This while loop allows user to input ticker symbols and quantities.
# list_ticker_inputs = []
# list_of_sectors = ["technology","consumer products","banking"]
# while True:
#     ticker_input = input("Please enter a stock ticker symbol: ").upper()
#     if ticker_input == "DONE":
#         break
    
#     quantity_input = float(input("Please enter the number of shares you own: "))
#     for i in list_of_sectors: print (i)
#     sector_input = input("Please enter the sector that most closely represents the stock: ").upper()
    
#     if ticker_input in list_ticker_inputs:
#         stk.Stock.stocks_data_frame['quantity'][ticker_input] += quantity_input
#     else:
#         new_stock = stk.Stock(ticker_input,quantity_input,sector_input)
#         list_ticker_inputs.append(ticker_input)

#     print('If you are done entering stocks, please type "Done" and then press enter.')

# Testing
list_of_sectors = ["information technology", "consumer staples", "financials", 
                  "communication services", "industrials", "healthcare",
                  "consumer discretionary", "energy", "materials", 
                  "utilities", "real estate", "other"]
goog = stk.Stock("wfc",  1, "financials")
amzn = stk.Stock("amzn", 2, "Consumer staples")
pins = stk.Stock("pins", 3, "information Technology")

stk.Stock.get_allocations()
portfolio = stk.Stock.stocks_data_frame
print(stk.Stock.stocks_data_frame.head())

allocation_by_sector = pd.DataFrame(index=list_of_sectors, columns=["allocation"])
for i in list_of_sectors:
    allocation_by_sector["allocation"][i] = portfolio["allocation"][portfolio['sector']==i].sum()
allocation_by_sector = allocation_by_sector.sort_values(by=["allocation"],ascending=True)
print(allocation_by_sector.head(12))

# Print out information about stock allocation and potential suggestions
print(f"{allocation_by_sector[]}")
