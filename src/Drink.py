import random
from functools import lru_cache


def get_drink():
    return random.choice(get_drinks())


@lru_cache(1)
def get_drinks():
    with open('../data/drinks.txt', 'r') as drinks_file:
        return [line.strip('\n') for line in drinks_file.readlines()]
