# Random DOG

Напишете програма, която показа снимка на произволно куче от сайта https://dog.ceo.
За целта трябва да направите заявка на към `url`: `https://dog.ceo/api/breed/<порода>/images/random`.
Напр.: https://dog.ceo/api/breed/samoyed/images/random.

След това от върнатия резултат трябва да извадите `url` на изображението и да покажете изображениете.
Как да се направи заявка и да се обработи резултата е описано в лекцията `Web APIs and JSON`.
За да го покажете стартирайте браузер с дадения `url` по този начин:

```python
import webbrowser
webbrowser.open(url)
```

# Валутен конвертор

Напишете функция `convert_currency`, която конвертира валута.
Функцията има три параметъра:

 - сума
 - валута в коята е сумата
 - валута, до която да се конвертира сумата

 Да се използва API-то на fixer.io (http://data.fixer.io/api/latest?access_key=df36769ca30746523ddcb41f1e0e7faa). Вижте примара в лекцията `Web APIs and JSON`.

 ```python
def convert_currency(amount, from_currency, to_currency):
    """
    >>> convert_currency(100, 'USD', 'BGN')
    172.46
    """
    pass
 ```