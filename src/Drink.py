import random
from functools import lru_cache


def get_drink() -> tuple[str, str]:
    return get_article(random.choice(random.choice(get_drinks())))


@lru_cache(1)
def get_drinks() -> list[list[str]]:
    with open('..\\data\\drinks.txt', 'r') as f:
        return [get_all_drinks_for_line(line) for line in f.readlines()]


def get_all_drinks_for_line(line: str) -> list[str]:
    return line.strip('\n').split(',')


def get_article(drink: str) -> tuple[str, str]:
    if '|' in drink:
        article, separator, drink_name = drink.partition('|')
        return article, drink_name

    return 'an' if drink[0] in 'aeiou' else 'a', drink
