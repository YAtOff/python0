def skip(f):
    return None


def volwels_count(s):
    """
    >>> volwels_count('hello')
    2
    >>> volwels_count('I\\'m fine')
    3
    """
    pass


@skip
def cons_count(s):
    """
    >>> cons_count('hello')
    3
    >>> cons_count('I\\'m fine')
    3
    """
    pass


@skip
def caps_count(s):
    """
    >>> caps_count('Hello')
    1
    >>> caps_count('PEP')
    3
    """
    pass


@skip
def all_caps(s):
    """
    >>> all_caps('PEP')
    True
    >>> all_caps('Python')
    False
    """
    pass


@skip
def snake_to_camel(s):
    """
    >>> snake_to_camel('snake_to_camel')
    'snakeToCamel'
    """
    pass


@skip
def snake_to_pascal(s):
    """
    >>> snake_to_pascal('snake_to_pascal')
    'SnakeToPascal'
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
