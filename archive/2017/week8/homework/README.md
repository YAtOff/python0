## Задача 1 - Числа в текст

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
    """ do it"
    pass


def teens_to_text(num):
    """ do it"
    pass


def hundreds_to_text(num):
    """ do it"
    pass
```
