import unittest

import requests
from pyumetric import NewRelic_Provider
from pyumetric import NewRelicInvalidApiKeyException
from pyumetric import NewRelicApiException
from pyumetric import NewRelicInvalidParameterException
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
    def test_ping(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        self.assertEqual(True, nr.ping())

    @patch('requests.get')
    def test_ping_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertEqual(False, nr.ping())

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
        self.assertRaises(NewRelicInvalidParameterException, lambda: nr.get_app(""))

    @patch('requests.get')
    def test_get_metrics(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_metrics(456)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_metrics_with_name(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_metrics(456, "Apdex")
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_metrics_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NewRelicApiException, lambda: nr.get_metrics(456))
        self.assertRaises(NewRelicInvalidParameterException, lambda: nr.get_metrics(""))

    @patch('requests.get')
    def test_get_metric_with_name_value(self, mock_get):
        mock_get.return_value.status_code = 200
        nr = NewRelic_Provider("123")
        response = nr.get_metric(456, ["WebTransaction"], ["average_response_time"], "2019-02-01T01:00:00+00:00", "2019-02-14T11:03:20+00:00", True)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_get_metric_error(self, mock_get):
        mock_get.return_value.status_code = 500
        nr = NewRelic_Provider("123")
        self.assertRaises(NewRelicInvalidParameterException, lambda: nr.get_metric("", ["WebTransaction"], ["average_response_time"]))
        self.assertRaises(NewRelicInvalidParameterException, lambda: nr.get_metric(456, [], ["average_response_time"]))
        self.assertRaises(NewRelicInvalidParameterException, lambda: nr.get_metric(456, ["WebTransaction"], []))
        self.assertRaises(NewRelicApiException, lambda: nr.get_metric(456, ["WebTransaction"], ["average_response_time"]))

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