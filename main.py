# First we use a function to test our function speeds

from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} seconds')
        return result
    return wrapper


#  Then we create a Fibonacci Sequence using a generator
@performance
def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + a

for x in fib(20):
  print (x)

# Then we create a Fibonacci Sequence using a list
@performance  
def fib2(number):
  a = 0
  b = 1
  result = []
  for i in range(number):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result

print(fib2(20))

# We can use our performance function to compare the function speeds



