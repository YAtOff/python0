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

    def intersection(self, other):
        """
        Връща общия диапазон между два.
        Използвайте `IntersectionRange`.
        """
        pass

    def union(self, other):
        """
        Връща обединение на два диапзона.
        Използвайте `UnionRange`.
        """
        pass


class IntersectionRange:
    def __init__(self, first, second):
        pass

    def includes(self, value):
        """
        Проверява дали стойността `value` е и в двата диапазона
        """
        pass


class UnionRange:
    def __init__(self, first, second):
        pass

    def includes(self, value):
        """
        Проверява дали стойността `value` е в поне един диапазон
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
>>> range2 = Range(5, 20)
>>> intersection = range.intersection(range2)
>>> intersection.includes(2)
>>> False
>>> intersection.includes(10)
True
>>> union = range.union(range2)
>>> uinon.includes(2)
>>> True
```