from datetime import datetime


def convert_to_datetime(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')


def convert_to_date(date_string):
    return convert_to_datetime(date_string).date()


def convert_to_timestamp(date_string):
    return convert_to_datetime(date_string).timestamp()


def convert_to_datetime_from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


def convert_to_date_from_timestamp(timestamp):
    return convert_to_datetime_from_timestamp(timestamp).date()


def convert_to_timestamp_from_datetime(date_time):
    return date_time.timestamp()


def convert_datetime_to_unix_timestamp(date_time):
    return int(date_time.timestamp())


def convert_date_string_to_unix_timestamp(date_string):
    return convert_datetime_to_unix_timestamp(convert_to_datetime(date_string))


def convert_unix_timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def convert_unix_timestamp_to_date_iso(timestamp):
    return convert_unix_timestamp_to_datetime(timestamp).date().isoformat()


def convert_datetime_now_to_unix_timestamp():
    return int(datetime.now().timestamp())
