def get_token():
    with open('../token.txt', 'r') as token_file:
        return token_file.readline().strip()
