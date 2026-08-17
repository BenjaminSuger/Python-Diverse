def hidden_word(secret: str, boards: str) -> bool:
    if not secret:
        return True
    value = 0
    i = 0
    while i < len(secret):
        if secret[i] in boards[value:]:
            value = boards.index(secret[i], value) + 1
        else:
            return False
        i += 1
    return True


print(hidden_word("aaaa","aaa"))
print(hidden_word("aab", "aaab"))
print(hidden_word("xyz", "abc"))
