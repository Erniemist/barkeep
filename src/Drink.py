import random
from functools import lru_cache


def get_drink():
    return random.choice(get_drinks())


@lru_cache(1)
def get_drinks():
    with open('..\\data\\drinks.txt', 'r') as f:
        return [line.strip('\n') for line in f.readlines()]
