def sanitise(string, safe_chars=None):
    if safe_chars is None:
        alphabet = 'abcdefghijiklmnopqrstuvwyz'
        safe_chars = "?.\"'" + alphabet + alphabet.upper()
    return str.join('', [char for char in string if char in safe_chars])
