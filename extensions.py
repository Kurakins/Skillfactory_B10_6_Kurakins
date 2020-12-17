import requests
import json
from config import keys, YOUR_KEY


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, quantity: str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}.')

        try:
            base = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}.')

        try:
            quantity = float(quantity)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {quantity}.')
        target = quote + '/' + base
        r = requests.get(f'http://api.currencies.zone/v1/quotes/{target}/json?quantity={quantity}&key={YOUR_KEY}')
        d = json.loads(r.content)
        return (d['result'].get('amount'))

