#ex1
import math

def Change(x):
    return (x * math.pi) / 180

inp_deg = float(input())
print(Change(inp_deg))

#ex2
def area_of_trapezoid(x, y, z):
    return (y + z) * x / 2


height = float(input("Height: "))
first_val = float(input("Base, first value: "))
second_val = float(input("Base, second value: "))
print("area of trapezoid:", area_of_trapezoid(height, first_val, second_val))

#ex3
import math

def cot(x):
    return 1 / math.tan(x)

def area(s, l):
    return 0.25 * s * l**2 * cot(math.pi / s) 

sides = int(input("Number of sides: "))
length = int(input("Length of a side: "))
print("Area of polygon:", area(sides, length))


#ex4
def area(x, y):
    return x * y


length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print("Area of parallelogram:", area(length, height))