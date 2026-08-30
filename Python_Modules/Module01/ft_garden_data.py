#!/usr/bin/python3

class Plant:
    def __init__(self, name="random", height="100", age="10"):
        self.__name = name
        self.__height = height
        self.__age = age

    def __str__(self):
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def show(self):
        print(self)


if __name__ == "__main__":
    garden = []
    garden.append(Plant("Rose", "25", "30"))
    garden.append(Plant("Sunflower", "80", "45"))
    garden.append(Plant("Cactus", "15", "120"))
    print("== Garden Plant Registry ===")
    for i in garden:
        i.show()
