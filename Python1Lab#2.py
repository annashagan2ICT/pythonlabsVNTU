correct_password = "starlink"

user_password = input("Введіть пароль: ")

if user_password == correct_password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
    