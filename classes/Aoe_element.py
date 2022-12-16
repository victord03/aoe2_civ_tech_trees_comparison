
class AoeElement:
    name: str
    cost: dict[str, int]

    # todo: requirements list ('Dark Age' for starting buildings / units)
    # todo: Age can be implemented as AoElement

    def __init__(self, name: str, cost: dict):
        self.name = name
        self.cost = cost
