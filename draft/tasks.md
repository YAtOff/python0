# Задача 1

Напишете функция `mean`, киято смята средно-аритметичната стойност на списък
от числа.

```python
>>> mean([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3])
2.54
>>> mean([2, 3, 2, 3])
2.50
>>> mean([3, 3, 3, 3, 3])
3.00
```

# Задача 2

Напишете функция `partition`, която разделя сиволен низ на `N` части.
Последнатч част може да е с рaзлична дължина от останалите.

```python
>>> partition("chew", 2)
["ch", "ew"]
>>> partition("thematic", 4)
["them", "atic"]
>>> partition("c++", 2)
["c+", "+"]
````


# Задача 3

Една поръчка в интернет магазин има следния формат:

```python
order = [
    {
        "product": "Nexus 5",
        "quantity": 1,
        "price_per_item": 799.99
    },
    {
        "product": "iPhone X",
        "quantity": 2,
        "price_per_item": 1000
    },
]
```
Напишете функция `free_shipping`, която проверява дали клиентът ще получи
безплатна доставка за дадена поръчка. Безплатна доставка има ако общата
сума на поръчката е над 2000.


# Задача 4

Напишете фунцкия `year_to_century`,  която приеама годна и връща век във
формат `<век>th century`.

```python
>>> century(1756)
"18th century"
>>> century(1555)
"16th century"
```

# Задача 5

Напишете функция `double_letters`, която връща `True`, ако в дадена дума
има повтарящи се букви една до друга.

```python
>>> double_letters("loop")
True
>>> double_letters("yummy")
True
>>> double_letters("orange")
False
```

# Задача 6

Напишете функция `is_symmetrical`, която връща `True`, ако дадено число
е симетрично (виж примера).

```python
>>> is_symmetrical(7227)
True
>>> is_symmetrical(12567)
False
>>> is_symmetrical(44444444)
True
```

# Задача 7

Напишете функция `is_valid_pin`, която приема пин-код като символен низ,
и връща `True`, ако пин-кода е валиден (състои се от 4 или 6 цифри).

```python
>>> is_valid_pin("1234")
True
>>> is_valid_pin("123456")
True
>>> is_valid_pin("12345")
False
>>> is_valid_pin("a234")
False
```

# Задача 8

Напишете функция `longest_zero`, която приема низ от нули и единици,
и връща най-дългата поредица от нули.

```python
>>> longest_zero("01100001011000")
"0000"
>>> longest_zero("100100100")
"00"
>>> longest_zero("11111")
""
```

# Задача 9

Напишете функция `get_extension`, която приема има на фаил и връща
разширението на файла.

```python
>>> get_extension("code.html")
"html"
```

# Задача 10

Напишете функция `sum_digits`, която пресмята сумата на всички цифри между две числа.
Напр.: за числа 19 и 22: (1 + 9) + (2 + 0) + (2 + 1) + (2 + 2) = 19

```python
>>> sum_digits(7, 8)
15
>>> sum_digits(17, 20)
29
>>> sum_digits(10, 12)
6
```

# Задача 11

Къде е Waldo? Напишете функция `whereiswaldo`, която връща кординатите ([ред, колона])
на енинствения различен елемент в матрица.

```python
>>> whereiswaldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
])
[3, 2]
>>> whereiswaldo([
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
])
[2, 4]
>>> whereiswaldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O ", "X"]
])
[3, 4]
```

# Задача 11

Напишете функция `replace_range`, която заменя диапазон от букви със `#`.
Диапазонът е във формат `<начална буква>-<крайна буква>`.

```python
>>> replace_range("abcdef", "c-e")
"ab###f"
>>> replace_range("rattle", "r-z")
"#a##le"
>>> replace_range("microscopic", "i-i")
"m#croscop#c"
>>> replace_range("", "a-z")
""
```

# Задача 12

Напишете функция `split_and_delimit`, коята приема символен низ, брой символи
и разделител, и разделя низа на дадения брой части, а след това го слепва
с разделителя.

```python
>>> split_and_delimit("bellow", 2, "&")
"be&ll&ow"
>>> split_and_delimit("magnify", 3, ":")
"mag:nif:y"
>>> split_and_delimit("poisonous", 2, "~")
"po~is~on~ou~s"
```

# Задача 13

Напишете функция `accumulating_product`, която приема списък с числа и връща
списък, с който всяко число е произведение от предишните.

```python
>>> accumulating_product([1, 5, 7])
[1, 5, 35]
>>> accumulating_product([1, 0, 1, 0])
[1, 0, 0, 0]
```

# Задача 14

Координатите на точка се представят в следния вид:

```python
point = {"x": 1, "y": 1}
```

А окръжност се представя в следния вид:
```python
circle = {
    "x": 3,
    "y": 3,
    "r": 10
}
```

Напишете функция `points_in_circle`, която приема кръг и списък с точки,
и връща броя точки, които влизат в кръга.

```python
>>> circle = {
    "x": 3,
    "y": 3,
    "r": 5
}
>>> points = [
    {"x": 5, "y": 5},
    {"x": 11, "y": 1},
]
>>> points_in_circle(circle, points)
1
```

# Задача 15

Нека картинка да се представя като матрица от единици и нули.
Напишете функция `reverse_image`, която обръща цветовете в картинката -
нулите стават единиц и обратно.

```python
>>> reverse_image([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])
[
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]
```

# Задача 16

Напишете функция `mexican_wave`, която прави мексиканска вълна от символен низ
(виж примера).

```python
>>> mexican_wave("mexican wave")
[
    "Mexican wave",
    "mExican wave",
    "meXican wave",
    "mexIcan wave",
    "mexiCan wave",
    "mexicAn wave",
    "mexicaN wave",
    "mexican wave",
    "mexican Wave",
    "mexican wAve",
    "mexican waVe",
    "mexican wavE"
]
```