from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today()
        delta = today_date - date_obj
        return delta.days
    except ValueError:
        # Якщо виникає помилка при перетворенні рядка у дату
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")
        return None


print(get_days_from_today("2024-04-10"))
