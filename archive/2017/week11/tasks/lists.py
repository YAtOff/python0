# -*- coding: utf-8 -*-

'''
# Задачи с обхождане на списък

## Задача 1 - Обхождане на списък.

Дефинирайто две различни функции - `for_traverse` и `while_traverse`,
които обхождат следния списък:

books = ["Learn You a Haskell",
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

* Едното обхождане трябва да е с `for ... in` обхождането
* Второто обхождане трябва да е с `while`
* Обхожданията трябва да отпечатат на екрана името на всяка книга на нов ред.

>>> for_traverse()
Learn You a Haskell
The Healthy Programmer
Code Complete
The Pragmatic Programmer
Pro Git
Introduction to Algorithms
Concrete Mathematics

>>> while_traverse()
Learn You a Haskell
The Healthy Programmer
Code Complete
The Pragmatic Programmer
Pro Git
Introduction to Algorithms
Concrete Mathematics


## Задача 2 - Броят на четните числа от всички в даден списък

Дефинирайте функция `evens_count`,
която приема като аргумент списък от цели числа и връща като резултат
броя четни числа в него.

>>> events_count([1, 2, 4])
2

## Задача 3 - Сумата на числата от списък

Дефинирайте функция `sum_numbers`,
която приема като аргумент списък от цели числа и връща като резултат
сумата им.

>>> sum_numbers([1, 2, 4])
7

## Задача 4 - Максималното число в списък

Дефинирайте функция `max_number`,
която приема като аргумент списък от цели числа и връща като резултат
най-голямото от тях.

>>> max_number([1, 2, 4])
4

## Задача 5 - Минимално число в списък

Дефинирайте функция `min_number`,
която приема като аргумент списък от цели числа и връща като резултат
най-малкото от тях.

>>> min_number([1, 2, 4])
1

## Задача 6 - Брой на срещания на дадена дума в списък от думи

Дефинирайте функция `words_count`,
която приема като аргумент списък от думи и дума,
и връща колко пъти се среща думата в списъка.

>>> words_count(['list', 'python', 'word'], 'word')
1
'''

books = ["Learn You a Haskell",
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]


def for_traverse():
    # your code here
    pass


def while_traverse():
    # your code here
    pass


def evens_count(numbers):
    # your code here
    pass


def sum_numbers(numbers):
    # your code here
    pass


def max_number(numbers):
    # your code here
    pass


def min_number(numbers):
    # your code here
    pass


def words_count(words, word):
    # your code here
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
