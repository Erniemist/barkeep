def sanitise(string, safe_chars=None):
    if safe_chars is None:
        safe_chars = "?.\"'" + str.join('', [chr(i) for i in range(ord('A'), ord('z') + 1)])
    return str.join('', [char for char in string if char in safe_chars])
