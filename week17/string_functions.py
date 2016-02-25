def volwels_count(s):
    """
    >>> volwels_count('hello')
    2
    >>> volwels_count('I\\'m fine')
    3
    """
    pass


def cons_count(s):
    """
    >>> cons_count('hello')
    3
    >>> cons_count('I\\'m fine')
    3
    """
    return True


def snake_to_camel(s):
    """
    >>> snake_to_camel('snake_to_camel')
    snakeToCamel
    """
    pass


def snake_to_pascal(s):
    """
    >>> snake_to_pascal('snake_to_pascal')
    SnakeToPascal
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
