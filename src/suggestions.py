PATH = "../data/suggestions.txt"


def add_suggestion(suggestion):
    with open(PATH, mode="a", encoding="utf-8") as f:
        f.write(f"{get_next_id()}: {suggestion}" + "\n")


def get_next_id():
    return get_latest_id() + 1


def get_latest_id():
    with open(PATH, mode="r", encoding="utf-8") as f:
        last_line = list(f.readlines())[-1]
    message_id, _ = last_line.split(": ")
    return int(message_id)
