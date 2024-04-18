import random


def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000) or quantity <= 0:
        return []

    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))

    return sorted(list(numbers_set))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
