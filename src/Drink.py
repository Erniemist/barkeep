import random
from functools import lru_cache
from dataclasses import dataclass


@dataclass
class Drink:
    article: str
    name: str


def get_drink() -> Drink:
    return random.choice(random.choice(get_drink_variants()))


@lru_cache(1)
def get_drink_variants():
    return [
        [
            hydrate(drink_text.strip('\n'))
            for drink_text in drink_line.split(',')
        ]
        for drink_line in get_drink_lines()
    ]


def hydrate(drink_text: str) -> Drink:
    if '|' in drink_text:
        article, separator, name = drink_text.partition('|')
    else:
        article, name = 'an' if drink_text[0] in 'aeiou' else 'a', drink_text

    return Drink(article, name)


def get_drink_lines() -> list[str]:
    with open('..\\data\\drinks.txt', 'r') as f:
        return list(f.readlines())


