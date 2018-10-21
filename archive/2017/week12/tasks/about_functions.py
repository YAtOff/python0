__ = "-=> FILL ME IN! <=-"


def assert_equal(expected, actual):
    assert expected == actual, '%r == %r' % (expected, actual)


def function_with_no_return():
    print('I have no return. What do I retrun?')


assert_equal(__, function_with_no_return())


def function_with_params(a, b):
    return a + b


assert_equal(2, function_with_params(__, __))

# keyword arguments

assert_equal(__, function_with_params(a=1, b=2))

# default parameters

def function_with_default_params(a, b=1):
    return a + b

assert_equal(__, function_with_default_params(1))
assert_equal(__, function_with_default_params(1, 2))
assert_equal(__, function_with_default_params(1, b=3))

# scope

x = 1
def func():
    x = 2  # NOQA

func()
assert_equal(__, x)


def func2():
    global x
    x = 2

func2()
assert_equal(__, x)


a = 1
b = 2
def func3(a, b):
    return a + b

assert_equal(__, func3(2, 2))