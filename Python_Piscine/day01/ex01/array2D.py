import numpy as np #temporaire je sais pas encore ce que je vais utiliser


def slice_me(family: list, start: int, end: int) -> list:
    family = np.asarray(family)
    print(f"My shape is : {family.shape}")
    family = family[start:end]
    print(f"My new shape is : {family.shape}")
    return family.tolist()

if __name__ == "__main__":
    pass
