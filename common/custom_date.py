import datetime


def get_custom_today(date_format='%Y-%m-%d'):
    now = datetime.datetime.now()
    return now.strftime(date_format)


def get_custom_tomorrow(date_format='%Y-%m-%d'):
    return get_custom_later_day(date_format, days=1)


def get_custom_later_day(date_format='%Y-%m-%d', days=6):
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days)
    return tomorrow.strftime(date_format)
