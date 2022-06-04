import random
from functools import lru_cache


def get_drink():
    return random.choice(get_drinks())


@lru_cache(1)
def get_drinks():
    with open('drinks.txt', 'r') as drinks_file:
        drinks = [line.strip('\n') for line in drinks_file.readlines()]
    return drinks
