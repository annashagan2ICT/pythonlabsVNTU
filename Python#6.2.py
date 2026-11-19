good_habits = {
    "today": [
        "Make a compliment to a friend",
        "Call your grandparents",
        "Embrace parents"
    ],
    "tomorrow": [
        "Feed the birds in the park",
        "Give unnecessary things to those who need them",
        "Smile"
    ]
}

for day, habits in good_habits.items():
    print(f"{day}:")
    for habit in habits:
        print(habit)