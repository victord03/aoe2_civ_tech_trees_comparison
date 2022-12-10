from classes.Aoe_element import AoeElement
from classes.Unit import Unit
from classes.Upgrade import Upgrade


class Building(AoeElement):
    # todo: where to specify the Man-at-Arms upgrade vs the Man-at-Arms unit?
    name: str
    cost: dict
    can_train: list[Unit]
    can_research: list[Upgrade]

    def __init__(self, name, cost):
        super().__init__(name, cost)
