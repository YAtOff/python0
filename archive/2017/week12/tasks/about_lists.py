__ = "-=> FILL ME IN! <=-"


def assert_equal(expected, actual):
    assert expected == actual, '%r == %r' % (expected, actual)


# creating lists
empty_list = list()
assert_equal(list, type(empty_list))
assert_equal(__, len(empty_list))

# list literals
nums = list()
assert_equal([], nums)

nums[0:] = [1]
assert_equal([1], nums)

nums[1:] = [2]
assert_equal([1, __], nums)

nums.append(333)
assert_equal([1, 2, __], nums)

# accessing list elements
noms = ['peanut', 'butter', 'and', 'jelly']

assert_equal(__, noms[0])
assert_equal(__, noms[3])
assert_equal(__, noms[-1])
assert_equal(__, noms[-3])

# slicing lists
noms = ['peanut', 'butter', 'and', 'jelly']

assert_equal(__, noms[0:1])
assert_equal(__, noms[0:2])
assert_equal(__, noms[2:2])
assert_equal(__, noms[2:20])
assert_equal(__, noms[4:0])
assert_equal(__, noms[4:100])
assert_equal(__, noms[5:0])

# slicing to the edge
noms = ['peanut', 'butter', 'and', 'jelly']

assert_equal(__, noms[2:])
assert_equal(__, noms[:2])

# lists and ranges
assert_equal(range, type(range(5)))
assert_equal([1, 2, 3, 4, 5], range(1, 6))
assert_equal(__, list(range(5)))
assert_equal(__, list(range(5, 9)))

# ranges with steps
assert_equal(__, list(range(5, 3, -1)))
assert_equal(__, list(range(0, 8, 2)))
assert_equal(__, list(range(1, 8, 3)))
assert_equal(__, list(range(5, -7, -4)))
assert_equal(__, list(range(5, -8, -4)))

# insertions
knight = ['you', 'shall', 'pass']
knight.insert(2, 'not')
assert_equal(__, knight)

knight.insert(0, 'Arthur')
assert_equal(__, knight)

# popping lists
stack = [10, 20, 30, 40]
stack.append('last')

assert_equal(__, stack)

popped_value = stack.pop()
assert_equal(__, popped_value)
assert_equal(__, stack)

popped_value = stack.pop(1)
assert_equal(__, popped_value)
assert_equal(__, stack)

# Notice that there is a "pop" but no "push" in python?

# Part of the Python philosophy is that there ideally should be one and
# only one way of doing anything. A 'push' is the same as an 'append'.

# To learn more about this try typing "import this" from the python
# console... ;)

