from src.drink import DrinkRepository


def test_get_drink():
    drink_repository = DrinkRepository(['a Coke'])
    drink = drink_repository.get_drink()
    assert drink == 'a Coke'
