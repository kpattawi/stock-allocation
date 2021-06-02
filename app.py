from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        ticker_input = request.form['ticker']
        quantity_input = request.form['quantity']
        sector_input = request.form['sector']
        if ticker_input == "":
            render_template(index.html, message="Please enter required fields.")
        print(ticker_input, quantity_input, sector_input)
        return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)