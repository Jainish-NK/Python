#get redius from user and find circle area using math lib

import math

radius = float(input("Enter The redius : "))

area = math.pi * math.pow(radius,2)

print(f"Area of the circle with radius {radius} is: {area:.2f}")

