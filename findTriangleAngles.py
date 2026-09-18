# calculating angles of triangle
import math


def calculate_angle(a, b, c):
    # Using the Law of Cosines to calculate the angle opposite side c
    angle_C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    return angle_C
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    return angle_B
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    return angle_A


print("Enter the lengths of the three sides of the triangle:")
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
print("Angle A:", calculate_angle(a, b, c))
print("Angle B:", calculate_angle(b, a, c))
print("Angle C:", calculate_angle(c, a, b))
