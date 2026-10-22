n = int(input())

r1 = [f"   ~   " for i in range(n)]
r2 = [f" (o o) " for i in range(n)]
r3 = [f" / V \\ " for i in range(n)]
r4 = [f"/( {i} )\\" for i in range(1, n + 1)]
r5 = [f"  ^^ ^^" for i in range(n)]

print(" ".join(r1))
print(" ".join(r2))
print(" ".join(r3))
print(" ".join(r4))
print(" ".join(r5))