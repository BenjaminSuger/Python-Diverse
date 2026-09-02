def count_in_list(content: list[str], word: str) -> int:
    """count element word inside the content"""
    count = 0
    for i in content:
        if i == word:
            count += 1
    return count
