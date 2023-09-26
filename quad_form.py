import math

a = float(input("Input the coefficient a: "))
b = float(input("Input the coefficient b: "))
c = float(input("Input the coefficient c: "))

delta = b ** 2 - 4 * a * c  # (delta)

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)  # FIRST ROOT
    x2 = (-b - math.sqrt(delta)) / (2 * a)  # 2ND ROOT
    print("Real solutions:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x1 = -b / (2 * a)  # Unique solution ( -b/2a )
    print("Unique solution:")
    print("x1 =", x1)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print("Complex solutions:")
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")
