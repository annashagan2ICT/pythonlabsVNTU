a = int(input())
b = int(input())

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd_val = x

lcm_val = abs(a * b) // gcd_val

print(lcm_val)