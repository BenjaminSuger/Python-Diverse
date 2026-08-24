def staircase_digits(lock: str) -> int:
    if not lock or len(lock) == 1:
        return 0
    count = 0
    for i in range(1, len(lock)):
        if lock[i].isdigit() and lock[i -1].isdigit() and int(lock[i - 1]) == int(lock[i]) - 1:
            count += 1
    return count

#staircase_digits("1a2b3c4") => 0
#staircase_digits("112233") => 2
#staircase_digits("019") => 1
