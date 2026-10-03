
day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік (2 цифри): "))

if day * month == year:
    print("The date is magic!")
else:
    print("This is a regular date.")