def extract_coins(amount, coin):
    """
    Ако от сумата (amount) може да се извадят монити от coin,
    отпечатва броя монети и връща остатъка от сумата
    """
    coins = amount // coin
    if coins != 0:
        print('{} * {}'.format(coins, coin))
    return amount % coin


def split_change(amount):
    """
    >>> split_change(7)
    1 * 5
    1 * 2

    >>> split_change(8)
    1 * 5
    1 * 2
    1 * 1

    >>> split_change(11)
    2 * 5
    1 * 1
    """
    rest = extract_coins(amount, 5)
    rest = extract_coins(rest, 2)
    extract_coins(rest, 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
