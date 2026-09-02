def NULL_not_found(object: any) -> int:
    match object:
        case float() if object != object:
            print(f"Cheese: {object} {type(object)}")
            return 0
        case bool() if not object:
            print(f"Fake: {object} {type(object)}")
            return 0
        case int() if not object:
            print(f"Zero: {object} {type(object)}")
            return 0
        case str() if not object:
            print(f"Empty:{object} {type(object)}")
            return 0
        case None:
            print(f"None: {object} {type(object)}")
            return 0
        case _:
            print("Type not Found")
            return 1


'''
On my version the order between bool() and int() matters as
python interpret True and False as int.
If we don't want to care about the order we cannot do it with a match case
(at least I did not find a way but with a different function
def NULL_not_found(object: any) -> int:
    if type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) is int and not object:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) is bool and not object:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif type(object) is str and not object:
        print(f"Empty:{object} {type(object)}")
        return 0
    elif object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
'''
