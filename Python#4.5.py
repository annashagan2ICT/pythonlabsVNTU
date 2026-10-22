s = input()
count = 0
correct = True
for char in s:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
        if count < 0:
            correct = False
            break
if count != 0:
    correct = False
print(correct)