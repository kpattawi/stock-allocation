import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta

import pandas_datareader.data as pdr



AVERAGE_TRADING_DAYS_PER_YEAR = 252



class Stock:

    stocks_data_frame = pd.DataFrame()

    def __init__(self, ticker, quantity, sector=None):
        """
        Method adds stock information (ticker, quantity, current price, current value) 
        to pandas dataframe with ticker as the index.
        """
        self.ticker = ticker.lower()
        self.quantity = quantity
        self.sector = sector.lower()
        self.current_price = pdr.DataReader(self.ticker, "yahoo", date.today()-timedelta(days=1), date.today())["Adj Close"][0]
        self.current_value = self.quantity*self.current_price
        stock_data = {"quantity":self.quantity,
                "price":self.current_price,
                "sector": self.sector,
                "current value":self.current_value,
                "annual mean":self.get_10yr_mean_annual_rets(),
                "annual std":self.get_10yr_std_annual_rets(),
                "allocation":None
                }
        new_stock_data_frame = pd.DataFrame(stock_data, index=[self.ticker])
        Stock.stocks_data_frame = Stock.stocks_data_frame.append(new_stock_data_frame)



    # These are methods that get single values such as mean and standard deviation.
    def get_10yr_mean_annual_rets(self):
        """Method returns mean annual returns based on past 10 years of data."""
        prices_10yr = pdr.DataReader(self.ticker, "yahoo", date.today()-timedelta(days=365*10), date.today())["Adj Close"]
        rets_10yr = prices_10yr.pct_change()[1:]    # Remove the first value because it is NaN.
        mean_annual_rets = rets_10yr.mean()*AVERAGE_TRADING_DAYS_PER_YEAR
        return mean_annual_rets

    def get_10yr_std_annual_rets(self):
        """Method returns standard deviation of annual returns based on past 10 years of data."""
        prices_10yr = pdr.DataReader(self.ticker, "yahoo", date.today()-timedelta(days=365*10), date.today())["Adj Close"]
        rets_10yr = prices_10yr.pct_change()[1:]          # Remove the first value because it is NaN.
        mean_annual_std = rets_10yr.std()*np.sqrt(AVERAGE_TRADING_DAYS_PER_YEAR)     # There are usually 252 trading days per year. 
        return mean_annual_std



    # These are methods that change the attributes of an instance of the Stock class.
    def add_to_position(self, quantity):
        """Method that increases size of position by adding to initial amount."""
        self.quantity = self.quantity + quantity
        return None



    # These are methods that return a pandas dataframe like historic price data.   
    def get_prices(self, start_date, end_date):
        """
        Method that returns a pandas dataframe with "Adj Close" prices
        from the start_date to the end_date.  This also initializes
        self.prices_adj_close
        """
        self.prices = pdr.DataReader(self.ticker, "yahoo", start_date, end_date)
        self.prices_adj_close = self.prices["Adj Close"]
        return self.prices_adj_close



    # The class methods for the Stock class.
    @classmethod
    def get_allocations(cls):
        """
        Class method that updates stocks_dataframe "Allocations" as a fraction, not a percent,
        to the stocks_data_frame. Note that this does not get updated when new Stock objects are created, only when method is called.
        """
        cls.stocks_data_frame["allocation"] = cls.stocks_data_frame["current value"].apply(lambda x: x/cls.stocks_data_frame["current value"].sum())


    @classmethod
    def empty_portfolio(cls):
        """
        Class method that updates stocks_dataframe "Allocations" as a fraction, not a percent,
        to the stocks_data_frame. Note that this does not get updated when new Stock objects are created, only when method is called.
        """
        Stock.stocks_data_frame = pd.DataFrame()
