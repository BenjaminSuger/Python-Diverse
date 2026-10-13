class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product"""
        result = 0
        for i in range(0, len(V1)):
            result += (V1[i] * V2[i])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add vector"""
        result = []
        for i in range(0, len(V1)):
            result.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substraction vector"""
        result = []
        for i in range(0, len(V1)):
            result.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is : {result}")
