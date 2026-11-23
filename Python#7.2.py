def repeat_string(text, n):
    return text * n

text = input("Enter word: ")
n = int(input("Enter count of copies: "))

print(repeat_string(text, n))