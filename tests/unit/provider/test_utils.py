import unittest
from pyumetric import Datetime_Utils
import pytz
from datetime import datetime, timedelta


class TestUtils(unittest.TestCase):

    def test_utils(self):
        self.assertEqual(
            (datetime.now(pytz.timezone("UTC")) + timedelta(days=1)).strftime("%m/%d/%Y, %H:%M:%S"),
            Datetime_Utils("UTC", 1).format("%m/%d/%Y, %H:%M:%S")
        )
        self.assertEqual(
            (datetime.now(pytz.timezone("UTC")) - timedelta(days=1)).strftime("%m/%d/%Y, %H:%M:%S"),
            Datetime_Utils("UTC", -1).format("%m/%d/%Y, %H:%M:%S")
        )
        self.assertEqual(
            (datetime.now(pytz.timezone("UTC"))).strftime("%m/%d/%Y, %H:%M:%S"),
            Datetime_Utils("UTC", 0).format("%m/%d/%Y, %H:%M:%S")
        )


if __name__ == "__main__":
    unittest.main()
