with open("stocks.csv", "r") as fs, open("output.csv", "w") as fo:
    fo.write("Company name,PE ratio,PB ratio\n")
    next(fs)
    for line in fs:
        tokens = line.split(",")
        name = tokens[0]
        price = float(tokens[1])
        earnings = float(tokens[2])
        value = float(tokens[3])
        peRatio = price/earnings
        priceBook = price/value
        fo.write(f"{name},{peRatio},{priceBook}\n")