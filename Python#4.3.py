s = input()
res = "".join(sorted(set(s.replace(" ", ""))))
print(res)