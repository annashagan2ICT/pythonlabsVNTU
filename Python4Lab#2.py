n = input("Введіть число: ")

integer_part, fractional_part = n.split(".")

new_number = float(f"{fractional_part}.{integer_part}")

print(new_number)