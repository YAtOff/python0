1. Атака на топ

Напишете функция `rook_can_capture`, която приема две позиции на шахматна
дъска и връща `True`, ако топ на позиция 1 може да атакува позиция 2.

```python
>>> rook_can_capture("A8", "E8")
True
>>> rook_can_capture("A1", "B2")
False
```

2. Филтриране по брой цифри

Напишете фунцкия `filter_by_digit_length`, която приема списък от числа и
брой цифри, по които да филтрира списъка. Функцията трябва да връща списък,
в който да присъстват само числа с дадения брой цифри.

```python
>>> filter_by_digit_length([123, 3456, 1, 68, 789], 3)
[123, 789]
```

3. Jackpot

Напишете функция `test_jackpot`, която приема списък от думи, и връща `True` ако всички
думи са еднакви.

```python
>>> test_jackpot(["$", "$", "$", "$", "$"])
True
>>> test_jackpot(["$", "$", "@", "$", "$"])
False
```

4. Subreddit

Напишете функция `sub_reddit`, която приема `url` на група в `Reddit`,
и връша името на групате (виж примерите).

```python
>>> sub_reddit("https://www.reddit.com/r/funny/")
"funny"
>>> sub_reddit("https://www.reddit.com/r/relationships/")
"relationships"
>>> sub_reddit("https://www.reddit.com/r/mildlyinteresting/")
"mildlyinteresting"
```

5. Процент -> Дроб

Напишете функция `percent_to_decimal`,
която приема стойност в проценти във формат `<number>%` (напр.: `10.1%`),
 и преобразува сторйноста в дроб (вижте примера).

```python
>>> percent_to_decimal("10.1%")
0.101
>>> percent_to_decimal("75%")
0.75
```