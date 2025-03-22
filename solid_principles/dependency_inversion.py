"""
The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.
"""

from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using FX API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using Alpha API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("EUR", "USD", 100)


if __name__ == "__main__":
    converter = AlphaConverter()
    app = App(converter)
    app.start()
