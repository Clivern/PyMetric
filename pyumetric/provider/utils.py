"""
Utils Class
"""

import pytz
from datetime import datetime, timedelta


class Datetime_Utils():

    def datetime(self, tz="UTC", diff_days=0):

        dt = datetime.now(pytz.timezone(tz))

        if diff_days > 0:
            dt += timedelta(days=diff_days)
        elif diff_days < 0:
            dt -= timedelta(days=(-1 * diff_days))

        return dt

    def to_iso(self, dt):
        return dt.isoformat()

    def format(self, dt, format):
        return dt.strftime(format)
