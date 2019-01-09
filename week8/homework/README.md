# Задача 1 - Ресто

Разполагате с неограничен брой банкноти от 1, 2 и 5 лева.
Напишете функция `split_change`, която:

* приема парична сума `change`
* извежда сумата като сбор от банкноти по 1, 2 и 5 лева.
Банкнотите трябва да бъдат минимален брой.
* Изписва на отделни редове брой банкноти и вид във формат (брой * вид)
* Приемете, че въведената сума може да се представи с наличните банкноти

Пример:

```python
>>> split_change(7)
1 * 5
1 * 2

>>> split_change(8)
1 * 5
1 * 2
1 * 1

>>> split_change(11)
2 * 5
1 * 1
```

# Задача 2 - валидни дати

Напишете функция `valid_data`, която проверява дали дадена дата е валидна. За да решите задачата по-лесно
дефинирайте отделно функция за проверка на всяка част
от датата. `valid_data` комбинира резултат от изпълнението
на всички функции.

```python
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
```

## Задача 3 - Числа в текст

Напишете функция `number_to_text`,
която приема цяло число в интервала [0..999]
и връща като резултат символен низ
съответстващ на английското произношение на числото.

Примери:

```python
number_to
>>> number_to_text(0)
zero
>>> number_to_text(4)
four
>>> number_to_text(14)
fourteen
>>> number_to_text(25)
twenty five
>>> number_to_text(400)
four houndred
>>> number_to_text(511)
five hundred and eleven
```

За целта използвайте функциите:

```python
def ones_to_text(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'


def tens_to_text(num):
    """ do it"""
    pass


def teens_to_text(num):
    """ do it"""
    pass


def hundreds_to_text(num):
    """ do it"""
    pass


def number_to_text(num):
    """do it"""
    pass
```
