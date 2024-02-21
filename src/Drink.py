import random
from functools import lru_cache
from dataclasses import dataclass
from typing import Self


def read_drinks_list() -> list[str]:
    with open('../data/drinks.txt', 'r') as f:
        return list(f.readlines())


class DrinkRepository:
    def __init__(self, drinks_list):
        self.drinks_list = drinks_list

    @classmethod
    @lru_cache(1)
    def make(cls) -> Self:
        """Makes a singleton instance of DrinkRepository"""
        return DrinkRepository(read_drinks_list())

    def get_drink(self) -> str:
        return random.choice(random.choice(self.get_drink_variants()))

    def get_drink_variants(self):
        return [
            [
                drink_text.strip('\n')
                for drink_text in drink_line.split(',')
            ]
            for drink_line in self.drinks_list
        ]
