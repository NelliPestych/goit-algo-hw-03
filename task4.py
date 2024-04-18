from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        # Перетворюємо рядок дати народження у об'єкт datetime
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Замінюємо рік на поточний рік
        birthday_date = birthday_date.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, переносимо його на наступний рік
        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточною датою
        days_until_birthday = (birthday_date - today).days

        # Переносимо дату народження на наступний понеділок, якщо вона припадає на вихідний
        if days_until_birthday <= 7:
            if birthday_date.weekday() == 5:  # Субота
                birthday_date += timedelta(days=2)
            elif birthday_date.weekday() == 6:  # Неділя
                birthday_date += timedelta(days=1)

            # Додаємо інформацію про користувача та дату привітання до списку upcoming_birthdays
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.04.19"},
    {"name": "Jane Smith", "birthday": "1990.04.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
