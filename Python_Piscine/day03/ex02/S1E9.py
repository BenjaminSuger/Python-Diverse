from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Character die"""
        self.is_alive = False


class Stark(Character):
    """Stark class inherit from Character abstract class"""
    def __init__(self, first_name, is_alive=True):
        """Stark constructor"""
        super().__init__(first_name, is_alive)


if __name__ == "__main__":
    pass
