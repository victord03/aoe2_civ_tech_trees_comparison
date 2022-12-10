from classes.Aoe_element import AoeElement
from classes.Unit import Unit
from classes.Upgrade import Upgrade


class Building(AoeElement):
    # todo: where to specify the Man-at-Arms upgrade vs the Man-at-Arms unit?
    can_train: list[Unit]
    can_research: list[Upgrade]

    def __init__(self, name, cost):
        self.cost = {"Food": 0, "Wood": 0, "Gold": 0, "Stone": 0}
        super().__init__(name, cost)
