# main.py
from flask import Flask, jsonify, request
from currency_converter import CurrencyConverter
from api_handler import APIHandler
from consts import *
app = Flask(__name__)

currency_converter = CurrencyConverter(currency_rates)
api_handler = APIHandler(currency_converter)

@app.route('/currencies', methods=['GET'])
def get_currencies():
    return jsonify(currency_rates)


@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount', 1.0))

    converted_amount = currency_converter.convert_currency(from_currency, to_currency, amount)

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    })


if __name__ == '__main__':
    app.run(debug=True)
