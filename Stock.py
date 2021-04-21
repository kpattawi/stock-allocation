# import modules for Stock class
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
import pandas_datareader.data as web

class Stock:
    stocks_dataFrame = pd.DataFrame()

    def __init__(self, ticker, quantity):
        self.ticker = ticker
        self.quantity = quantity
        self.currentPrice = web.DataReader(self.ticker, "yahoo", date.today()-timedelta(days=1), date.today())['Adj Close'][0]
        self.currentValue = self.quantity*self.currentPrice
        Stock.stocks_dataFrame = pd.DataFrame.append(Stock.stocks_dataFrame,pd.DataFrame({"Quantity": self.quantity, "Price": self.currentPrice, "Current Value": self.currentValue}, index=[self.ticker]))

    @classmethod
    def get_allocation(cls):
        return cls.stocks_dataFrame["Current Value"].apply(lambda x: x/cls.stocks_dataFrame["Current Value"].sum())

    @classmethod
    def get_currentTotalValue(cls):
        return cls.stocks_dataFrame["Current Value"].sum()

    def get_prices(self,startDate,endDate):
        self.prices = web.DataReader(self.ticker, "yahoo", startDate, endDate)
        self.prices_adjClose = self.prices['Adj Close']
        return self.prices_adjClose
