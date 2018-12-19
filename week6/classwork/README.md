# Guess the nuber

Крайната цел на това упражнение е да се реализира играта "Guess the number".
Играта има следните правила:

- програмата намисля число от 1 до 10
- играчът трябва да познае числото, като има на разположение три опита
- ако го познае: изписва се съобщение "You win!"
- в противен случай: "You loose!"
- след всяка игра програмата пита дали играчът иска да изиграе още една
  игра
- при потвърждение всичко се повтаря
- в противен случай изпълнението на програмата приключва

Например:

```
Guess the number: 1
Guess the number: 5
You win!
Do you want to play again? no
Good buy!
```

```
Guess the number: 3
Guess the number: 9
Guess the number: 7
You loose!
Do you want to play again? yes
Guess the number: 4
Guess the number: 8
You win!
Do you want to play again? no
Good buy!
```
"""

Програмата може да измисли произволно число по следния начин:

```
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 10
number = str(randint(MIN_NUMBER, MAX_NUMBER))
```
