def get_token():
    with open('../token.txt', 'r') as f:
        return f.readline().strip()
