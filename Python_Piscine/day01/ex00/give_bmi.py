from numpy import multiply


def check_input(input: list[int | float]) -> bool:
    """check the input needs to be a list and int or float"""
    if not isinstance(input, list):
        return False
    breakpoint()
    for i in input:
        if not isinstance(i, float) and not isinstance(i, int):
            return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give the bmi with multiplication from numpy"""
    #check if the input is good
    





def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """for each element in bmi check the limit"""
    #il faut bien maitriser les histoire de comparaison int avec float pour etre sur comment ca marche (parce que 2 = 1.99999) donc la il y a un gros piege 
    pass

if __name__ == "__main__":
    print(check_input([3,4,5,6.0, 'a']))
