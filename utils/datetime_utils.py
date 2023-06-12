from datetime import datetime, timedelta
from dateutil import relativedelta


def get_current_datetime():
    return datetime.now()


def get_formatted_datetime(fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(fmt)


def modify_datetime(dt, years=0, months=0, days=0, hours=0):
    delta = relativedelta.relativedelta(years=years, months=months)
    dt += delta
    dt += timedelta(days=days, hours=hours)
    return dt
