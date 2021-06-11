from math_series.series import fibonacci, lucas, sum_series

# Fibonacci Tests

def test_one():
    actual = fibonacci(7)
    expected = 8
    assert actual == expected

def test_two():
    actual = fibonacci(9)
    expected = 21
    assert actual == expected

# Lucas Tests

def test_three():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_four():
    actual = lucas(10)
    expected = 123
    assert actual == expected

# Sum Series Tests

def test_five():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_six():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected
