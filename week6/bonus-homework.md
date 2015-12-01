## Задача 1 - Числа в текст

Във файл, който се казва `number_text.py`, напишете функция `number_to_text`,
която приема цяло число в интервала [0..999] и връща като резултат символен низ
съответстващ на английското произношение на числото.

Примери:

```python
number_to
>>> number_to_text(0)
Null
>>> number_to_text(4)
Four
>>> number_to_text(14)
Fourteen
>>> number_to_text(25)
Twenty five
>>> number_to_text(400)
Four houndred
>>> number_to_text(511)
Five hundred and eleven
```
## Задача 2 - Валидатор на дати

Във файл `valid_date.py`, напишете функция `date_is_valid`, 
която приема дата под формата на: година, месец, ден, час, минута, секунда;
и връща `True` ако датата е влидна и `False` в противен случай.

```python
def data_is_valid(year, month, day, hour, minute, second):
    # вашето решение
```

```python
>>> data_is_valid(2015, 1, 2, 23, 20, 10)
True
>>> data_is_valid(2015, 2, 29, 12, 10, 10)
False
>>> data_is_valid(2012, 2, 29, 12, 10, 10)
True
>>> data_is_valid(2015, 11, 31, 13, 30, 50)
False
```
