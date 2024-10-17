stocks = {
    "info": [600,630,620],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160]
}

def print_all():
    for stock, n in stocks.items():
        avg = 0
        j = 0
        for i in n:
           avg += i
           j += 1
        avg = avg/j
        print(f"{stock} ==> {n} ==> {avg}")
def add_stock():
    s = input("enter the name of new stock: ")
    p = float(input("enter the stock price: "))
    if s in stocks:
        print("stock already exists, I appended new value.")
        stocks[s].append(p)
    else:
        stocks[s] = [p]
print_all()
add_stock()
print_all()