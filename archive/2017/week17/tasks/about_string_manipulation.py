__ = "-=> FILL ME IN! <=-"


def assert_equal(expected, actual):
    assert expected == actual, '%r == %r' % (expected, actual)


def assert_not_equal(expected, actual):
    assert expected != actual, '%r != %r' % (expected, actual)


# use format to interpolate variables
value1 = 'one'
value2 = 2
string = "The values are {0} and {1}".format(value1, value2)
assert_equal(__, string)

# formatted values can be shown in any order or be repeated
value1 = 'doh'
value2 = 'DOH'
string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
assert_equal(__, string)

# any python expression may be interpolated
import math # import a standard python module with math functions

decimal_places = 4
string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
    decimal_places)
assert_equal(__, string)

# you can get a substring from a string
string = "Bacon, lettuce and tomato"
assert_equal(__, string[7:10])

# you can get a single character from a string
string = "Bacon, lettuce and tomato"
assert_equal(__, string[1])

# single characters can be represented by integers
assert_equal(__, ord('a'))
assert_equal(__, ord('b') == (ord('a') + 1))

# strings can be split
string = "Sausage Egg Cheese"
words = string.split()
assert_equal([__, __, __], words)

# strings can be split by char
string = "the,rain,in,spain"
words = string.split(',')

assert_equal([__, __, __, __], words)

# Pattern is a Python regular expression pattern which matches ',' or ';'

# raw strings do not interpret escape characters
string = r'\n'
assert_not_equal('\n', string)
assert_equal(__, string)
assert_equal(__, len(string))

# Useful in regular expressions, file paths, URLs, etc.

# strings can be joined
words = ["Now", "is", "the", "time"]
assert_equal(__, ' '.join(words))

# strings can change case
assert_equal(__, 'guido'.capitalize())
assert_equal(__, 'guido'.upper())
assert_equal(__, 'TimBot'.lower())
assert_equal(__, 'guido van rossum'.title())
assert_equal(__, 'ToTaLlY aWeSoMe'.swapcase())
