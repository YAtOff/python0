1. Фермерски проблем

Имате информация за животните в една ферма под формата на речник,
като ключовете са видът животно (може да е пиле, прасе или заек),
а стойностиете са броя животни от даден вид. Напр.:

```python
animals = {"пиле": 100, "прасе": 20, "заек": 50}
```

Напишете фунцкия `count_legs`, която приема речника с животни като параметър
и връща общия брой крака на животни във фермата.

2. Четни и нечетни

Напишете функция `partition_odd_even`, която разделя един списък от числа на
два - първият съдържа само нечетни числа, а вторият - само четни.
Функцията трябва да връща като резултат списък, съдържащ двате списъка.

```python
>>> partition_odd_even([1, 2, 3, 4, 5])
[[1, 3, 5], [2, 4]]
```

3. is_in_range

Напишете функция `is_in_range`, която приема число и речник със ключове
`max` и `min`,  и връща `True` ако числото е в диапазона `[min, max]`.

```python
>>> is_in_range(1, {"min": 0, "max": 3})
True
```

4. Наставка

Напишете функция `add_endings`, която приема спъск от думи и наставка,
и връща нов списък със същите думи, но с наставката добавена накрая.

```python
>>> add_ending(["clever", "meek", "hurried", "nice"], "ly")
["cleverly", "meekly", "hurriedly", "nicely"]
```

5. Повторение

Напишете функция `repeat`, която приема символен низ и число `N`,
и връща съмволен низ, в който всеки символ се повтаря `N` пъти.

```python
>>> repeat("hello", 5)
hhhhheeeeellllllllllooooo
```
