from data.upgrades import upgrades_data
from data.units import units as units_data


class Building:
    """Class representing each Civ building.

    The goal is to track all building info separately and also assign available units and researches here, for
    ease of use."""

    name: str
    cost: dict

    available_units: dict
    available_researches: dict

    hp: int
    line_of_sight: int
    build_time: int

    def __init__(self, name: str, cost: dict, hp: int, line_of_sight: int, build_time: int):
        """Init method.

        Requires the above arguments to differentiate each building.

        The remaining attributes are set using other methods."""

        self.name = name
        self.cost = cost
        self.available_units = dict()
        self.available_researches = dict()
        self.hp = hp
        self.line_of_sight = line_of_sight
        self.build_time = build_time

    def assign_available_units(self, units: list[str]):
        """Given a units list, which is a list of names, assigns those units as available to the building.

        It creates a new key entry to the available_units attribute using the name of the unit provided in
        the list, and then fetches all the data associated with that unit by executing a lookup in the
        data.units.py data file for the corresponding key bearing the same unit name.

        Store it in the attribute, effectively creating a dict containing the data, as a value to the original key."""

        for each_unit in units:
            self.available_units[each_unit] = units_data[each_unit]

    def assign_available_researches(self, researches: list[str]):
        """Given a researches list, which is a list of names, assigns those researches as available to the
        building.

        It creates a new key entry to the available_researches attribute using the name of the research provided in
        the list, and then fetches all the data associated with that research by executing a lookup in the
        data.upgrades.py data file for the corresponding key bearing the same research / upgrade name.

        Store it in the attribute, effectively creating a dict containing the data, as a value to the original key."""

        for each_research in researches:
            self.available_researches[each_research] = upgrades_data[each_research]
