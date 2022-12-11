from classes.Aoe_element import AoeElement
from classes.Unit import Unit
from classes.Upgrade import Upgrade


class Building(AoeElement):
    # todo: where to specify the Man-at-Arms upgrade vs the Man-at-Arms unit?
    name: str
    cost: dict

    available_units: list[Unit]
    available_researches: list[Upgrade]

    # hp: int
    # line_of_sight: int
    # build time: int

    def __init__(self, name, cost):
        super().__init__(name, cost)

    def assign_available_units(self):
        ...

    def assign_available_researches(self):
        ...
