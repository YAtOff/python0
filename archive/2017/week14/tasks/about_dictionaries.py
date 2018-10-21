
__ = "-=> FILL ME IN! <=-"


def assert_equal(expected, actual):
    assert expected == actual, '%r == %r' % (expected, actual)


# creating dictionaries

empty_dict = dict()
assert_equal(dict, type(empty_dict))
assert_equal({}, empty_dict)
assert_equal(__, len(empty_dict))

# dictionary literals
empty_dict = {}
assert_equal(dict, type(empty_dict))
babel_fish = { 'one': 'uno', 'two': 'dos' }
assert_equal(__, len(babel_fish))

# accessing_dictionaries
babel_fish = { 'one': 'uno', 'two': 'dos' }
assert_equal(__, babel_fish['one'])
assert_equal(__, babel_fish['two'])

# changing dictionaries
babel_fish = { 'one': 'uno', 'two': 'dos' }
babel_fish['one'] = 'eins'

expected = { 'two': 'dos', 'one': __ }
assert_equal(expected, babel_fish)

# dictionary is unordered
dict1 = { 'one': 'uno', 'two': 'dos' }
dict2 = { 'two': 'dos', 'one': 'uno' }

assert_equal(__, dict1 == dict2)


# dictionary keys and values
babel_fish = {'one': 'uno', 'two': 'dos'}
assert_equal(__, len(babel_fish.keys()))
assert_equal(__, len(babel_fish.values()))
assert_equal(__, 'one' in babel_fish.keys())
assert_equal(__, 'two' in babel_fish.values())
assert_equal(__, 'uno' in babel_fish.keys())
assert_equal(__, 'dos' in babel_fish.values())

# making a dictionary from a sequence of keys
cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

assert_equal(__, len(cards))
assert_equal(__, cards['green elf'])
assert_equal(__, cards['yellow dwarf'])
