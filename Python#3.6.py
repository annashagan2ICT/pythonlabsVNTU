
import math
a = int(input("1 number:"))
b = int(input("2 number:"))

D = a**2 - 4 * b

x1 = int((a - math.isqrt(D)) // 2)
x2 = int((a + math.isqrt(D)) // 2)

print(f"{min(x1, x2)} {max(x1, x2)}")