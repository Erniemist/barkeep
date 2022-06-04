import random

drinks = []


def get_drink():
    global drinks
    if len(drinks) == 0:
        with open('drinks.txt', 'r') as drinks_file:
            drinks = [line.strip('\n') for line in drinks_file.readlines() if line != '\n']
    return random.choice(drinks)
