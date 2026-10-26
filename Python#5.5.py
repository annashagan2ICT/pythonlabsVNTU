s = input()
print(max(int(s[:i] + s[i+1:]) for i in range(len(s))))