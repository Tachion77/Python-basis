class Fibonacci:
    def __init__(self, limit):
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.limit:
            result = self.current + self.previous
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration
        
fibonacci_iterator = iter(Fibonacci(5))
while True:
    try:
        print(next(fibonacci_iterator))
    except StopIteration:
        break