s=input()
char=input()

if char not in s:
    print("missing")
else:
    first= s.find(char)
    last= s.rfind(char)
    if first == last:
        print("first")
    else:
        print(f"{first} {last}")