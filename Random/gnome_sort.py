def count_vowel(word: str) -> int:
    count = 0
    for i in word.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count

def helper_choice(first: str, second: str) -> bool:
    if len(first) > len(second):
        return True
    elif len(first) < len(second):
        return False
    if first.lower() > second.lower():
        return True
    elif first.lower() < second.lower():
        return False
    if count_vowel(first) > count_vowel(second):
        return True
    else:
        return False
    
def seed_packet_sort(labels: list[str]) -> list[str]:
    if len(labels) == 0 or len(labels) == 1:
        return labels
    i = 0
    while i < len(labels):
        if  i+1 < len(labels) and helper_choice(labels[i], labels[i+1]):
            labels[i] , labels[i + 1] = labels[i + 1], labels[i]
            if i > 0:
                i -= 1
        else:
            i += 1
    return labels
