# Диапазон

Дефинаирайте клас `Range`, които моделира диапазона от числа между
две стойности `(begin, end)`.

```python
class Range:
    def __init__(self, begin, end):
        # ...
        pass

    def __repr___(self):
        return '({}, {})'.format(self.begin, self.end)

    def includes(self, value):
        """
        Проверява дали стойността `value` е в диапазоне (begin, end)
        """
        pass

```

Примери:

```python
>>> range = Range(1, 10)
>>> range.includes(3)
True
>>> range.includes(11)
False
```