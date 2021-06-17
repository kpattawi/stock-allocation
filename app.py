import pandas as pd

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import stock as stk



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    stk.Stock.empty_portfolio()
    if request.method == 'POST':
        ticker_input1 = request.form['ticker1']
        if ticker_input1 == "":
            render_template(index.html, message="Please enter required fields.")
        quantity_input1 = float(request.form['quantity1'])
        sector_input1 = request.form['sector1']
        s = stk.Stock(ticker_input1, quantity_input1, sector_input1)
        ticker_input2 = request.form['ticker2']
        quantity_input2 = float(request.form['quantity2'])
        sector_input2 = request.form['sector2']
        stk.Stock(ticker_input2, quantity_input2, sector_input2)
        # ticker_input3 = request.form['ticker3']
        # quantity_input3 = request.form['quantity3']
        # sector_input3 = request.form['sector3']
        # stk.Stock(ticker_input3, quantity_input3, sector_input3)
        # ticker_input4 = request.form['ticker4']
        # quantity_input4 = request.form['quantity4']
        # sector_input4 = request.form['sector4']
        # stk.Stock(ticker_input4, quantity_input4, sector_input4)
        # ticker_input5 = request.form['ticker5']
        # quantity_input5 = request.form['quantity5']
        # sector_input5 = request.form['sector5']
        # stk.Stock(ticker_input5, quantity_input5, sector_input5)
        # ticker_input6 = request.form['ticker6']
        # quantity_input6 = request.form['quantity6']
        # sector_input6 = request.form['sector6']
        # stk.Stock(ticker_input6, quantity_input6, sector_input6)
        # ticker_input7 = request.form['ticker7']
        # quantity_input7 = request.form['quantity7']
        # sector_input7 = request.form['sector7']
        # stk.Stock(ticker_input7, quantity_input7, sector_input7)
        # ticker_input8 = request.form['ticker8']
        # quantity_input8 = request.form['quantity8']
        # sector_input8 = request.form['sector8']
        # stk.Stock(ticker_input8, quantity_input8, sector_input8)
        # ticker_input9 = request.form['ticker9']
        # quantity_input9 = request.form['quantity9']
        # sector_input9 = request.form['sector9']
        # stk.Stock(ticker_input9, quantity_input9, sector_input9)
        # ticker_input10 = request.form['ticker10']
        # quantity_input10 = request.form['quantity10']
        # sector_input10 = request.form['sector10']
        # stk.Stock(ticker_input10, quantity_input10, sector_input10)
        # print(ticker_input1, quantity_input1, sector_input1)

        s.get_allocations()
        allocations = stk.Stock.stocks_data_frame

        sector_categories = ['Communication Services', 'Consumer Discretionary', 
                            'Consumer Staples', 'Energy', 'Financials', 
                            'Healthcare', 'Industrials', 'Information Technology', 
                            'Materials', 'Real Estate', 'Utilities','Other'
                            ]
        sectors = pd.DataFrame(index=sector_categories, columns=['Sector'])
        for category in sector_categories:
            sum = allocations['allocation'][allocations['sector']==category].sum()
            sectors[category] = sum
        sectors = sectors.sort_values(by=['Sector'])
        
        
        return render_template('portfolio.html', tables=[allocations.to_html(classes='data')], titles=allocations.columns.values)
        


if __name__ == '__main__':
    app.run(debug=True)