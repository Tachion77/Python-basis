def calculate_area(base, height, shape=""):
    if shape == "triangle":
        area = base*height*1/2
    elif shape == "rectangle":
        area = base*height
    else:
        print("Error: there is no shape like that.")
    return area

def print_pattern(number):
    for i in range(n):
        s = ""
        for j in range(i+1):
            s = s + "*"
        print(s)

print("Which function you want to call?")
func = input()
if func == "calculate_area":
    print("Insert base, height adn then shape of your figure:")
    base = int(input())
    height = int(input())
    shape = input()
    area = calculate_area(base, height, shape)
    print("Area of your " + shape, "is:", area)
elif func == "print_pattern":
    print("Insert the number for lenght of your pattern:")
    n = int(input())
    print_pattern(n)
