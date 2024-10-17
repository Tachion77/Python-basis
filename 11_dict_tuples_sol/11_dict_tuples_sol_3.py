import math

def circle_calc(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    diameter = 2*radius
    return area, circumference, diameter

r = float(input("please eneter the radius: "))
area, circumference, diameter = circle_calc(r)
print(f"area: {area}, circumference: {circumference}, diameter: {diameter}")