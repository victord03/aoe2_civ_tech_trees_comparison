from classes.Building import Building


class Civ:

    bonus: dict[str: int]
    buildings: list[Building]

    def __init__(self):
        self.bonus = dict()
        self.buildings = list()

    def compare_to_another_civ(self, other_civ):
        self.compare_units()
        self.compare_upgrades()

    def compare_units(self):
        ...

    def compare_upgrades(self):
        ...

    def create_civ_baseline(self):

        # Dark Age

        self.buildings.append(Building("House", {"Wood": 25}))
        self.buildings.append(Building("Mining Camp", {"Wood": 100}))
        self.buildings.append(Building("Lumber Camp", {"Wood": 100}))
        self.buildings.append(Building("Mill", {"Wood": 100}))
        self.buildings.append(Building("Siege Workshop", {"Wood": 150}))
        self.buildings.append(Building("Barracks", {"Wood": 175}))
        self.buildings.append(Building("Outpost", {"Wood": 25, "Stone": 5}))
        self.buildings.append(Building("Palisade Wall", {"Wood": 5}))
        self.buildings.append(Building("Palisade Gate", {"Wood": 30}))

        # Feudal Age

        self.buildings.append(Building("Blacksmith", {"Wood": 150}))
        self.buildings.append(Building("Blacksmith", {"Wood": 175}))
        self.buildings.append(Building("Archery Range", {"Wood": 175}))
        self.buildings.append(Building("Stables", {"Wood": 175}))
        self.buildings.append(Building("Watch Tower", {"Wood": 50, "Stone": 125}))
        self.buildings.append(Building("Gate", {"Stone": 30}))
        self.buildings.append(Building("Stone Wall", {"Stone": 5}))

        # Castle Age

        self.buildings.append(Building("Monastery", {"Wood": 175}))
        self.buildings.append(Building("Siege Workshop", {"Wood": 200}))
        self.buildings.append(Building("University", {"Wood": 200}))
        self.buildings.append(Building("Castle", {"Stone": 650}))
        self.buildings.append(Building("Town Center", {"Wood": 275, "Stone": 100}))

        # Imperial Age

        self.buildings.append(Building("Wonder", {"Wood": 1000, "Gold": 1000, "Stone": 1000}))


    def create_teutons(self):
        ...
