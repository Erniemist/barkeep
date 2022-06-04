path = '..\\data\\suggestions.txt'


def add_suggestion(suggestion):
    with open(path, 'a') as f:
        f.write(f'{get_next_id()}: {suggestion}' + '\n')


def get_next_id():
    return get_latest_id() + 1


def get_latest_id():
    with open(path, 'r') as f:
        last_line = list(f.readlines())[-1]
    message_id, message = last_line.split(': ')
    return int(message_id)
