grades = input().split()
count_a = grades.count('A')
total = len(grades)
share = count_a / total
print(f"{share:.2f}")