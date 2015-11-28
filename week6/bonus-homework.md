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
## Задача 2 - Спирала

Във файл `spiral.py`, напишете функция `spiral`, 
която за положително цяло число `number (number < 20)` 
отпечатва матрица с числа като на фигурата по-долу.

```python
>>> spiral(4)
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7
```

За да се изведе число в две позиции, използвайте форматиращ низ `%2d`.
