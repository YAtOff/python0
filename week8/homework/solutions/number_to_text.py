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
    if num == 2:
        return 'twenty'
    if num == 3:
        return 'thirty'
    if num == 4:
        return 'fourty'
    if num == 5:
        return 'fifty'
    if num == 6:
        return 'sixty'
    if num == 7:
        return 'seventy'
    if num == 8:
        return 'eighty'
    if num == 9:
        return 'ninety'


def teens_to_text(num):
    if num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'


def hundreds_to_text(num):
    return ones_to_text(num)


def number_to_text(num):
    if num < 10:
        return ones_to_text(num)
    elif num < 20:
        return teens_to_text(num)
    elif num < 100:
        tens = tens_to_text(num // 10)
        if num % 10 > 0:
            return tens + ' ' + ones_to_text(num % 10)
        else:
            return tens
    elif num < 1000:
        hundreds = hundreds_to_text(num // 100)
        if num % 100 > 0:
            return hundreds + ' hundred and ' + number_to_text(num % 100)
        else:
            return hundreds + ' hundred'


assert number_to_text(0) == 'zero'
assert number_to_text(5) == 'five'
assert number_to_text(11) == 'eleven'
assert number_to_text(30) == 'thirty'
assert number_to_text(45) == 'fourty five'
assert number_to_text(300) == 'three hundred'
assert number_to_text(501) == 'five hundred and one'
assert number_to_text(111) == 'one hundred and eleven'
assert number_to_text(245) == 'two hundred and fourty five'

