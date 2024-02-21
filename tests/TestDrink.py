import unittest
from src.Drink import DrinkRepository


class MyTestCase(unittest.TestCase):
    def test_something(self):
        drink_repository = DrinkRepository(['Coke'])
        drink = drink_repository.get_drink()
        self.assertEqual(f"{drink.article} {drink.name}", 'a Coke')


if __name__ == '__main__':
    unittest.main()
