# Дробни числа

Дефинаирайте клас `Fraction`, който представлява обикновн дроб.
Конструктурът на клас приема два параметъра: числител и занменател.
Дефинирайте операциите събиране, изваждане, умножение и делене.
Като предефинирате операциите `+, -, *, /` [(тук има повече информация как)](https://realpython.com/operator-function-overloading/?fbclid=IwAR0wv9vv8EN0jZcLBC7OG-WN-KWJdLMsucrUNyzK6b7X2qYZ3guRT6_BvTM).


```python
class Fraction:
    def __init__(self, numerator, denominator):
        # ....
        pass

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        """
        Връща нов Fraction, който е сумата на текущия и `other`
        """
        # ....
        pass

    def __sub__(self, other):
        # ....
        pass

    def __mul__(self, other):
        # ....
        pass

    def __div__(self, other):
        # ....
        pass

```

Примери:

```python
>>> a = Fraction(1, 3)
>>> a
1/3
>>> b = Fraction(1, 2)
>>> b
1/2
>>> a + b
5/6
```