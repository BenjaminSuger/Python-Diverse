#no check of the from_base.....did not care that much
def convert_base(code: str, from_base: int, to_base: int) -> str:
    if (to_base > 36) or (to_base < 2):
        return "ERROR"
    try:
        value = int(code, from_base)
        if value == 0:
            return "0"
    except Exception as e:
        return "ERROR"
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while value > 0:
        result.append(base[value % to_base])
        value //= to_base
    return ''.join(reversed(result))
