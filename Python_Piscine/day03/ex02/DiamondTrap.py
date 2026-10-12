from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """King constructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        """Set eyes color"""
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """Set hairs color"""
        self.hairs = color

    def get_eyes(self) -> str:
        """Getter eyes color"""
        return self.eyes

    def get_hairs(self) -> str:
        """Getter hairs color"""
        return self.hairs
