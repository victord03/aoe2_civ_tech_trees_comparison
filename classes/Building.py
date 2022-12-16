from classes.Aoe_element import AoeElement
from data.upgrades import upgrades


class Building(AoeElement):
    # todo: where to specify the Man-at-Arms upgrade vs the Man-at-Arms unit?
    name: str
    cost: dict

    available_units: dict
    available_researches: dict

    hp: int
    line_of_sight: int
    build_time: int

    def __init__(self, name, cost, hp: int, line_of_sight: int, build_time: int):
        super().__init__(name, cost)
        self.available_units = dict()
        self.available_researches = dict()
        self.hp = hp
        self.line_of_sight = line_of_sight
        self.build_time = build_time

    def assign_available_units(self, units: dict):
        # self.available_units = units
        ...

    def assign_available_researches(self, researches: list):

        for each_research in researches:
            self.available_researches[each_research] = upgrades[each_research]
