import unittest

import requests
from pyumetric import NewRelic_Provider
from pyumetric import NewRelicInvalidApiKeyException
from pyumetric import NewRelicApiException
from unittest.mock import patch


class TestNewRelic(unittest.TestCase):

    @patch('requests.get')
    def test_get_apps(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_apps()
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_apps_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NewRelicApiException, lambda: nr.get_apps())

    @patch('requests.get')
    def test_get_app(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_app(456)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_app_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NewRelicApiException, lambda: nr.get_app(456))

    @patch('requests.get')
    def test_get_metrics(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_metrics(456)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_metrics_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NewRelicApiException, lambda: nr.get_metrics(456))

    @patch('requests.get')
    def test_get_metric_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NotImplementedError, lambda: nr.get_metric())

    def test_get_headers(self):
        nr = NewRelic_Provider("123")
        self.assertEqual(nr.get_headers(), {
            'X-Api-Key': "123"
        })

    def test_get_headers_error(self):
        nr = NewRelic_Provider("")
        self.assertRaises(NewRelicInvalidApiKeyException, lambda: nr.get_headers())


if __name__ == "__main__":
    unittest.main()