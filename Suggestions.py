def add_suggestion(suggestion):
    with open('suggestions.txt', 'a') as suggestions_file:
        suggestions_file.write(f'{get_next_id()}: {suggestion}' + '\n')


def get_next_id():
    return get_latest_id() + 1


def get_latest_id():
    with open('suggestions.txt', 'r') as suggestions_file:
        last_line = list(suggestions_file.readlines())[-1]
    message_id, message = last_line.split(': ')
    return int(message_id)
