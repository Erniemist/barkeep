import random
from functools import lru_cache


def get_drink() -> tuple[str, str]:
    drink = random.choice(random.choice(get_drinks()))
    return get_article(drink), drink


@lru_cache(1)
def get_drinks() -> list[list[str]]:
    with open('..\\data\\drinks.txt', 'r') as f:
        return [line.strip('\n').split(',') for line in f.readlines()]


def get_article(drink: str) -> str:
    if '|' in drink:
        return drink.partition('|')[0]

    return 'an' if drink[0] in 'aeiou' else 'a'
