1. Напишете програма, която приема число от клавиатурата и отпечатва абсолютната стойност на числото.

```
    > numbar: -1
    1

    > number: 1
    > 1
```

2. Напишете програма, която приема число от клавиатурата и отпечатва дали то е четно или нечетно:

```
    > numbar: 1
    odd

    > number: 2
    > even
```
Подсказка:
```
num % 2 == 0 за четно
num % 2 == 1 за нечетно
```

3. Напишете програма, която намира най-голямото по стойност число, измежду две дадени числа.

```
    > number 1: 1
    > number 2: 3
    3
```

4. Напишете програма, която намира най-малкото по стойност число, измежду две дадени числа.

```
    > number 1: 1
    > number 2: 3
    1
```
5. Напишете програма, която приема цифра (0-9) от клавиатурата и връща името на цифрата на английски език.

```
    > digit: 2
    two

    > digit: 5
    five
```

6. Напишете програма, която намира знака (+ или -) от произведението на две числа, без да го пресмята.

```
    > number 1: 1
    > number 2: 3
    +

    > number 1: 1
    > number 2: -3
    -
```

Подсказка:

Забранено е използването на умножение.
Използвайте селдните свойства на умножението.

| x | y | product |
-------------------
| + | + |    +    |
-------------------
| - | + |    -    |
-------------------
| + | - |    -    |
-------------------
| - | - |    +    |
-------------------


Напомням, че когато четете нещо от клавиатурате с `input`, то е текст (дори да
изглежда като число).

```
num = input('number: ')

print (num + 1)  # това е грешка, чащтото не може да събиреате текст (num) с число (1)
```

За да използвате въведената стойност като число, трябва да го преобразувате
с функцията `int`.


```
num = input('number: ')
num = int(num)

print (num + 1)  # това е OK
```