from classes.Aoe_element import AoeElement


class Unit(AoeElement):
    name: str
    cost: dict

    def __init__(self, name, cost):
        super().__init__(name, cost)
