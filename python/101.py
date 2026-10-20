import math

number = 49

if number >= 0 and math.isqrt(number) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")