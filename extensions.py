import requests
import json
from config import keys, YOUR_KEY


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}.')
#        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
#       r = requests.get(f'http://api.currencies.zone/v1/quotes/EUR/USD/json?quantity=1&key=6390|244HCbTXQSqz~R^v~uFsJjP4_f9UOUe6')
        r = requests.get(f'http://api.currencies.zone/v1/quotes/{target}/json?quantity={quantity}&key={YOUR_KEY}')
#       print(r.text)
        d = json.loads(r.content)
        return (d['result'].get('source'), d['result'].get('target'), d['result'].get('value'))

    #        return total_base
