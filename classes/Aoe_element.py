
class AoeElement:
    name: str
    cost: dict[str, int]

    def __init__(self, name: str, cost: dict):
        self.name = name
        self.cost = cost
