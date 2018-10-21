def number_to_text(num):
    """
    Числа в текст

    Напишете функция `number_to_text`,
    която приема цяло число в интервала [0..999]
    и връща като резултат символен низ
    съответстващ на английското произношение на числото.

    >>> number_to_text(0)
    'zero'
    >>> number_to_text(4)
    'four'
    >>> number_to_text(14)
    'fourteen'
    >>> number_to_text(25)
    'twenty five'
    >>> number_to_text(400)
    'four hundred'
    >>> number_to_text(511)
    'five hundred and eleven'
    """
    hundreds = num // 100
    num = num % 100
    text = ''
    if num <= 9:
        text = ones_to_text(num)
    elif 10 <= num <= 19:
        text = teens_to_text(num)
    else:
        tens = num // 10
        num = num % 10
        text = tens_to_text(tens * 10)
        if 0 < num:
            text += ' ' + ones_to_text(num)

    if 0 < hundreds:
        if text == 'zero':
            return hundreds_to_text(hundreds * 100)
        else:
            return hundreds_to_text(hundreds * 100) + ' and ' + text
    else:
        return text


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
    """
    >>> tens_to_text(20)
    'twenty'
    >>> tens_to_text(50)
    'fifty'
    """
    if num == 20:
        return 'twenty'
    elif num == 30:
        return 'thirty'
    elif num == 40:
        return 'forty'
    elif num == 50:
        return 'fifty'
    elif num == 60:
        return 'sixty'
    elif num == 70:
        return 'seventy'
    elif num == 80:
        return 'eighty'
    elif num == 90:
        return 'ninety'


def teens_to_text(num):
    """
    >>> teens_to_text(11)
    'eleven'
    >>> teens_to_text(15)
    'fifteen'
    """
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
    """
    >>> hundreds_to_text(100)
    'one hundred'
    >>> hundreds_to_text(500)
    'five hundred'
    >>>
    """
    return ones_to_text(num // 100) + ' hundred'


if __name__ == '__main__':
    import doctest
    doctest.testmod()