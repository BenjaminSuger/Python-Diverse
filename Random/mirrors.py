def mirror_list(shelves: list[list[int]]) -> list[list[int]]:
    new_list = []
    for i in shelves:
        new_list.append(i[::-1])
    return new_list
