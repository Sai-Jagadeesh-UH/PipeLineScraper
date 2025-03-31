from dataclasses import dataclass
import re
import datetime
from datetime import date


@dataclass
class vc():
    key: str
    items: list
    combstring: list


# (till_hour=None, till_minute=None, till_time=None, quadrant=4, duration_hour=0, duration_minute=10, duration_time=None)
class argValidator():
    def __init__(self, args):
        self.from_date = args.fro
        self.till_date = args.till
        self.on_date = args.on

        self._Combs = {
            "t": vc("t",
                    [self.on_date],
                    ['o']),

            "f": vc("f",
                    [self.on_date],
                    ['o']),

            "o": vc("o",
                    [self.from_date, self.till_date],
                    ['f", "t'])
        }

    def getString(self):

        # 2324
        if any([self.from_date, self.till_date]) and not all([self.from_date, self.till_date]):
            return f" -t and -f cannot be used in isolation"

        if self.from_date and any(self._Combs['f'].items):
            return f"{self._Combs['f'].key} cannot be used with {self._Combs['f'].combstring}"

        if self.till_date and any(self._Combs['t'].items):
            return f"{self._Combs['t'].key} cannot be used with {self._Combs['t'].combstring}"

        if self.on_date and any(self._Combs['o'].items):
            return f"{self._Combs['o'].key} cannot be used with {self._Combs['o'].combstring}"

        return self.dataValidity()

    def is_valid_date(date_string, date_format):
        try:
            datetime.datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False

    def dataValidity(self):

        delta90 = datetime.timedelta(days=90)

        if self.from_date:
            if argValidator.is_valid_date(self.from_date, r"%m%d%Y"):
                if datetime.datetime.strptime(self.from_date, r"%m%d%Y").date() > date.today():
                    return "'-f' cannot be in future"
                if datetime.datetime.strptime(self.from_date, r"%m%d%Y").date() < date.today() - delta90:
                    return "'-f' cannot be more than 90 days past from today"
            else:
                return "please provide '-f' in valid mmddyyyy format"

        if self.till_date:
            if argValidator.is_valid_date(self.till_date, r"%m%d%Y"):
                if datetime.datetime.strptime(self.till_date, r"%m%d%Y").date() < datetime.datetime.strptime(self.from_date, r"%m%d%Y").date():
                    return "'-t' cannot be prior to '-f'"
                if datetime.datetime.strptime(self.till_date, r"%m%d%Y").date() > date.today():
                    return "'-t' cannot be in future"
                if datetime.datetime.strptime(self.till_date, r"%m%d%Y").date() < date.today() - delta90:
                    return "'-t' cannot be more than 90 days past from today"
            else:
                return "please provide '-t' in valid mmddyyyy format"

        if self.on_date:
            if argValidator.is_valid_date(self.on_date, r"%m%d%Y"):
                if datetime.datetime.strptime(self.on_date, r"%m%d%Y").date() > date.today():
                    return "'-o' cannot be in future"
                if datetime.datetime.strptime(self.on_date, r"%m%d%Y").date() < date.today() - delta90:
                    return "'-o' cannot be more than 90 days past from today"
            else:
                return "please provide '-o' in valid mmddyyyy format"

        return None
