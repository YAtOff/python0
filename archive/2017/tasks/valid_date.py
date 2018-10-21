def valid_second(second):
    """
    >>> valid_second(5)
    True
    >>> valid_second(66)
    False
    """
    pass

def valid_minute(minute):
    """
    >>> valid_minute(5)
    True
    >>> valid_minute(-1)
    False
    """
    pass

def valid_hour(hour):
    """
    >>> valid_hour(3)
    True
    >>> valid_hour(25)
    False
    """
    pass

def is_leap(year):
    """
    >>> is_leap(2000)
    True
    >>> is_leap(1999)
    False
    """
    pass

def valid_day(day, month, year):
    """
    >>> valid_day(1, 1, 2016)
    True
    >>> valid_day(31, 4, 2015)
    False
    >>> valid_day(29, 2, 2016)
    True
    >>> valid_day(29, 2, 2016)
    False
    """
    pass

def valid_month(month):
    """
    >>> valid_month(1)
    True
    >>> valid_month(15)
    False
    """
    pass

def valid_year(year):
    """
    >>> valid_year(2001)
    True
    >>> valid_year(-100)
    False
    """
    pass

def data_is_valid(year, month, day, hour, minute, second):
    return valid_second(second) and \
        valid_minute(minute) and \
        valid_hour(hour) and \
        valid_day(day, month, year) and \
        valid_month(month) and \
        valid_year(year)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
