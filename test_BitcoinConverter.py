import unittest
from unittest import TestCase
from unittest.mock import patch

import BitcoinConverter


class TestBitcoinConverter(TestCase):
    @patch('BitcoinConverter.requestRate')
    def testBitcointoDollar(self, mock_rates):
        mock_rates = 12345.67
        exampleApiResponse = {"bpi": {
            "USD": {
                "code": "USD",
                "symbol": "&#36;",
                "rate": "41,435.59",
                "description": "United States Dollar",
                "rate_float": mock_rates}
        }}
        mock_rates.side_effects = [exampleApiResponse]
        convert = BitcoinConverter.convert_bitcoin_to_dollars(100, mock_rates)
        self.assertEqual(12345.67, convert)


if __name__ == '__main__':
    unittest.main()
