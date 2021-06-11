def fibonacci(num):
  return sum_series(num)

def lucas(num):
  return sum_series(num)

def sum_series_iterative(num, a=0, b=1):
  if num == 0:
    return a

  if num == 1:
    return b

  for i in range(2, num + 1):
    c = a + b
    a = b
    b = c

  return c
