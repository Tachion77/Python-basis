def next_square():
    n = 1
    while True:
        yield n*n
        n += 1

square = next_square()

for x in range(10):
    print(next(square))
