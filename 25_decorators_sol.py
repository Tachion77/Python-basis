def decorator(func):
    def check(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise Exception("Argument is not a non-negative integer")
    return check

@decorator
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))