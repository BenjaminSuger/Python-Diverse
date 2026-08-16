#A == a so lower() required
#did on total but I could lenght could assume / 2 I think
def palyndrome_like(label: str) -> bool:
    if not label:
        return False
    new_str = label.replace(" ", "")
    return new_str.lower() == new_str[::-1].lower()
