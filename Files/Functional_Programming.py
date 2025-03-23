#1. Higher-Order Functions
#is a function that takes another function as an arguments or returns a function

from functools import reduce

# map(): Apply a function to each element in an iterable
numbers = [1 ,2 ,3 ,4, 5]
squared = list(map(lambda x : x ** 2 ,numbers))
print("Squared: ",squared)

# filter(): Select elements based on a conditions (case)
even = list(filter(lambda x: x % 2 == 0,numbers))
print("Even: ",even)

# reduce(): Apply a function on all elements as multiply all elements
product = reduce(lambda x,y: x * y,numbers)
print("Products: ",product)



#2.Lambdas (Anonymous Functions)
#is a small anonymous function defined using the lambda keyword
add_lambda = lambda a, b: a + b
print("Addition: ", add_lambda(3, 5))

# add_lambda = lambda a, b: a + b is equivalent to
# def add(a, b):
    #return a + b

# 3.Generators and Iterators
# Generators generates values lazily, meaning they don't store the entire sequence in memory, The "yield" keyword is used to produce values one at a time

def counter_usage(n):
    count  = 1
    while count <= n:
        yield count # stores one by one not all of them
        count += 1

generator = counter_usage(6)
for i in generator:
    print(i)
