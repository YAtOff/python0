def valid_second(second):
    return 0 <= second <= 59


assert valid_second(5)
assert not valid_second(66)


def valid_minute(minute):
    return 0 <= minute <= 59


assert valid_minute(5)
assert not valid_minute(-1)


def valid_hour(hour):
    return 0 <= hour <= 23


assert valid_hour(3)
assert not valid_hour(25)


def is_leap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


assert is_leap(2000)
assert not is_leap(1999)
assert not is_leap(1900)


def valid_day(day, month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 1 <= day <= 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 1 <= day <= 30
    elif is_leap(year):
        return 1 <= day <= 29
    else:
        return 1 <= day <= 28


assert valid_day(1, 1, 2016)
assert not valid_day(31, 4, 2015)
assert valid_day(29, 2, 2016)
assert not valid_day(29, 2, 2017)


def valid_month(month):
    return 0 <= month <= 12


assert valid_month(1)
assert not valid_month(15)


def valid_year(year):
    return year > 0


assert valid_year(2001)
assert not valid_year(-100)


def date_is_valid(year, month, day, hour, minute, second):
    return valid_second(second) and \
        valid_minute(minute) and \
        valid_hour(hour) and \
        valid_day(day, month, year) and \
        valid_month(month) and \
        valid_year(year)


assert date_is_valid(2019, 1, 22, 20, 20, 20)
assert not date_is_valid(2019, 2, 29, 20, 20, 20)
