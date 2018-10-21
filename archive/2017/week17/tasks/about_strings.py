__ = "-=> FILL ME IN! <=-"


def assert_equal(expected, actual):
    assert expected == actual, '%r == %r' % (expected, actual)


# double quoted strings are strings
string = "Hello, world."
assert_equal(__, isinstance(string, str))

# single quoted strings are also strings
string = 'Goodbye, world.'
assert_equal(__, isinstance(string, str))

# triple quote strings are also strings
string = """Howdy, world!"""
assert_equal(__, isinstance(string, str))

# triple single quotes work too
string = '''Bonjour tout le monde!'''
assert_equal(__, isinstance(string, str))

# raw strings are also strings
string = r"Konnichi wa, world!"
assert_equal(__, isinstance(string, str))

# use single quotes to create string with double quotes
string = 'He said, "Go Away."'
assert_equal(__, string)

# use double quotes to create strings with single quotes
string = "Don't"
assert_equal(__, string)

# use backslash for escaping quotes in strings
a = "He said, \"Don't\""
b = 'He said, "Don\'t"'
assert_equal(__, (a == b))

# use backslash at the end of a line to continue onto the next line
string = "It was the best of times,\n\
as the worst of times."
assert_equal(__, len(string))

# triple quoted strings can span lines
string = """
Howdy,
world!
"""
assert_equal(__, len(string))

# triple quoted strings need less escaping
a = "Hello \"world\"."
b = """Hello "world"."""
assert_equal(__, (a == b))

# escaping quotes at the end of triple quoted string
string = """Hello "world\""""
assert_equal(__, string)

# plus concatenates strings
string = "Hello, " + "world"
assert_equal(__, string)

# adjacent strings are concatenated automatically
string = "Hello" ", " "world"
assert_equal(__, string)

# plus will not modify original strings
hi = "Hello, "
there = "world"
string = hi + there
assert_equal(__, hi)
assert_equal(__, there)

# plus equals will append to end of string
hi = "Hello, "
there = "world"
hi += there
assert_equal(__, hi)

# plus equals also leaves original string unmodified
original = "Hello, "
hi = original
there = "world"
hi += there
assert_equal(__, original)

# most strings interpret escape characters
string = "\n"
assert_equal('\n', string)
assert_equal("""\n""", string)
assert_equal(__, len(string))

# a character in string can be accesses like in list

string = "Hello"
assert_equal(__, string[1])

# you can check weather a character is in string

string = "Hello"
assert_equal(__, 'H' in string)
assert_equal(__, 'Z' in string)