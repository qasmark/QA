import unittest
from unittest.mock import MagicMock
from currency_converter import CurrencyConverter
from api_handler import APIHandler


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        self.converter = CurrencyConverter(self.currency_rates)

    def test_convert_currency(self):
        from_currency = "USD"
        to_currency = "EUR"
        amount = 100

        converted_amount = self.converter.convert_currency(from_currency, to_currency, amount)

        self.assertAlmostEqual(converted_amount, 100 * (80.2 / 70.5), places=2)

    def test_convert_currency_with_missing_currency(self):
        from_currency = "USD"
        to_currency = "CAD"

        with self.assertRaises(ValueError):
            self.converter.convert_currency(from_currency, to_currency, 100)

    def test_convert_currency(self):
        currency_rates = {
            "USD": 70.5,
            "EUR": 80.2,
            "GBP": 90.8,
            "JPY": 0.64,
            "AUD": 50.6,
            "CAD": 55.3,
            "CHF": 72.9,
            "CNY": 10.2,
            "INR": 1.0,
            "RUB": 1.0,
            "KRW": 0.062,
            "BRL": 13.4
        }

        for from_currency, from_rate in currency_rates.items():
            for to_currency, to_rate in currency_rates.items():
                converter = CurrencyConverter(currency_rates)
                amount = 100

                converted_amount = converter.convert_currency(from_currency, to_currency, amount)

                expected_amount = amount * (to_rate / from_rate)
                self.assertAlmostEqual(converted_amount, expected_amount, places=2)


class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        self.converter_mock = MagicMock()
        self.converter_mock.currency_rates = self.currency_rates
        self.handler = APIHandler(self.converter_mock)

    def test_get_currency_rate(self):
        currency_code = "USD"

        result = self.handler.get_currency_rate(currency_code)

        self.assertEqual(result, 70.5)

    def test_get_currency_rate_with_missing_currency(self):
        currency_code = "CAD"

        with self.assertRaises(ValueError):
            self.handler.get_currency_rate(currency_code)

    def test_convert_same_currency(self):
        currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        converter = CurrencyConverter(currency_rates)

        converted_amount = converter.convert_currency("USD", "USD", 100)

        self.assertAlmostEqual(converted_amount, 100, places=2)

    def test_convert_zero_amount(self):
        currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        converter = CurrencyConverter(currency_rates)

        converted_amount = converter.convert_currency("USD", "EUR", 0)

        self.assertAlmostEqual(converted_amount, 0, places=2)

    def test_get_currency_rate(self):
        currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        converter = CurrencyConverter(currency_rates)
        handler = APIHandler(converter)

        result = handler.get_currency_rate("USD")

        self.assertEqual(result, 70.5)

    def test_get_currency_rate_with_missing_currency(self):
        currency_rates = {"USD": 70.5, "EUR": 80.2, "GBP": 90.8}
        converter = CurrencyConverter(currency_rates)
        handler = APIHandler(converter)

        with self.assertRaises(ValueError):
            handler.get_currency_rate("CAD")


if __name__ == '__main__':
    unittest.main()
