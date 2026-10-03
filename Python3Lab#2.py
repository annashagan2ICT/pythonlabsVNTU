x1 = int(input("x1:"))
y1 = int(input("y1:"))

x2 = int(input("x2:"))
y2 = int(input("y2:"))

px = int(input("x точки: "))
py = int(input("y точки: "))

if x1 <= px <= x2 and y2 <= py <= y1:
    print("Yes")
else:
    print("No")