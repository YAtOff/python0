# -*- coding: utf-8 -*-

def skip(f):
    return None


def for_traverse():
    """
    books = ["Learn You a Haskell",
            "The Healthy Programmer",
            "Code Complete",
            "The Pragmatic Programmer",
            "Pro Git",
            "Introduction to Algorithms",
            "Concrete Mathematics"]

    * Обхожданията трябва да отпечатат на екрана името на всяка книга на нов ред.

    >>> for_traverse()
    Learn You a Haskell
    The Healthy Programmer
    Code Complete
    The Pragmatic Programmer
    Pro Git
    Introduction to Algorithms
    Concrete Mathematics
    """
    pass


@skip
def while_traverse():
    """
    books = ["Learn You a Haskell",
            "The Healthy Programmer",
            "Code Complete",
            "The Pragmatic Programmer",
            "Pro Git",
            "Introduction to Algorithms",
            "Concrete Mathematics"]

    * Обхожданията трябва да отпечатат на екрана името на всяка книга на нов ред.

    >>> while_traverse()
    Learn You a Haskell
    The Healthy Programmer
    Code Complete
    The Pragmatic Programmer
    Pro Git
    Introduction to Algorithms
    Concrete Mathematics
    """
    pass


@skip
def evens_count(numbers):
    """
    Дефинирайте функция `evens_count`,
    която приема като аргумент списък от цели числа и връща като резултат
    броя четни числа в него.

    >>> events_count([1, 2, 4])
    2
    """
    pass


@skip
def sum_numbers(numbers):
    """
    Дефинирайте функция `sum_numbers`,
    която приема като аргумент списък от цели числа и връща като резултат
    сумата им.

    >>> sum_numbers([1, 2, 4])
    7
    """
    pass


@skip
def max_number(numbers):
    """
    Дефинирайте функция `max_number`,
    която приема като аргумент списък от цели числа и връща като резултат
    най-голямото от тях.

    >>> max_number([1, 2, 4])
    4
    """
    pass


@skip
def min_number(numbers):
    """
    Дефинирайте функция `min_number`,
    която приема като аргумент списък от цели числа и връща като резултат
    най-малкото от тях.

    >>> min_number([1, 2, 4])
    1
    """
    pass


@skip
def words_count(words, word):
    """
    Дефинирайте функция `words_count`,
    която приема като аргумент списък от думи и дума,
    и връща колко пъти се среща думата в списъка.

    >>> words_count(['list', 'python', 'word'], 'word')
    1
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
