from classes.Building import Building


class Civilization:

    bonus: dict[str: int]
    buildings: dict

    def __init__(self):
        """Init method for the Civilization class.

        Initiates the attributes bonus and buildings as empty dicts."""
        self.bonus = dict()
        self.buildings = dict()

    def compare_to_another_civ(self, other_civ) -> tuple:
        """Compares this Civilization instance to another one.

        Requires another Civilization instance passed as a parameter."""

        this_civ_units = self.get_all_available_units()
        other_civ_units = other_civ.get_all_available_units()

        this_civ_upgrades = self.get_all_available_upgrades()
        other_civ_upgrades = other_civ.get_all_available_upgrades()

        diff_units = set(this_civ_units) - set(other_civ_units)
        diff_upgrades = set(this_civ_upgrades) - set(other_civ_upgrades)

        return diff_units, diff_upgrades

    def get_all_available_units(self) -> list:
        """Gathers a list of all the available units for this Civ, for the purposes of comparing."""
        return list()

    def get_all_available_upgrades(self) -> list:
        """Gathers a list of all the available upgrades for this Civ, for the purposes of comparing."""
        return list()

    def create_non_meso_civilization_building_baseline(self):
        """Allocates buildings available to all non-meso civilizations.

        Creates all buildings that are available to all the civilizations and stores them inside in the buildings
        class attribute."""

        # Dark Age

        house = Building(name="House", cost={"Wood": 25}, hp=550, line_of_sight=2, build_time=25)
        self.buildings["House"] = house

        mining_camp = Building(name="Mining Camp", cost={"Wood": 100}, hp=600, line_of_sight=6, build_time=35)
        self.buildings["Mining Camp"] = mining_camp

        lumber_camp = Building(name="Lumber Camp", cost={"Wood": 100}, hp=600, line_of_sight=6, build_time=35)
        self.buildings["Lumber Camp"] = lumber_camp

        mill = Building(name="Mill", cost={"Wood": 100}, hp=600, line_of_sight=6, build_time=35)
        self.buildings["Mill"] = mill

        dock = Building(name="Dock", cost={"Wood": 150}, hp=1_800, line_of_sight=6, build_time=35)
        self.buildings["Dock"] = dock

        barracks = Building(name="Barracks", cost={"Wood": 175}, hp=1_200, line_of_sight=6, build_time=50)
        self.buildings["Barracks"] = barracks

        outpost = Building(name="Outpost", cost={"Wood": 25, "Stone": 5}, hp=500, line_of_sight=6, build_time=15)
        self.buildings["Outpost"] = outpost

        palisade_wall = Building(name="Palisade Wall", cost={"Wood": 5}, hp=150, line_of_sight=2, build_time=7)
        self.buildings["Palisade Wall"] = palisade_wall

        palisade_gate = Building(name="Palisade Gate", cost={"Wood": 30}, hp=600, line_of_sight=6, build_time=35)
        self.buildings["Palisade Gate"] = palisade_gate

        # Feudal Age

        blacksmith = Building(name="Blacksmith", cost={"Wood": 150}, hp=1_800, line_of_sight=6, build_time=40)
        self.buildings["Blacksmith"] = blacksmith

        market = Building(name="Market", cost={"Wood": 175}, hp=1_800, line_of_sight=6, build_time=60)
        self.buildings["Market"] = market

        archery_range = Building(name="Archery Range", cost={"Wood": 175}, hp=1_500, line_of_sight=6, build_time=50)
        self.buildings["Archery Range"] = archery_range

        stable = Building(name="Stable", cost={"Wood": 175}, hp=1_500, line_of_sight=6, build_time=50)
        self.buildings["Stable"] = stable

        watch_tower = Building(name="Watch Tower", cost={"Wood": 50, "Stone": 125}, hp=850, line_of_sight=10, build_time=80)
        self.buildings["Watch Tower"] = watch_tower

        gate = Building(name="Gate", cost={"Stone": 30}, hp=1_650, line_of_sight=6, build_time=70)
        self.buildings["Gate"] = gate

        stone_wall = Building(name="Stone Wall", cost={"Stone": 5}, hp=1_080, line_of_sight=2, build_time=10)
        self.buildings["Stone Wall"] = stone_wall

        # Castle Age

        monastery = Building(name="Monastery", cost={"Wood": 175}, hp=2_100, line_of_sight=6, build_time=40)
        self.buildings["Monastery"] = monastery

        siege_workshop = Building(name="Siege Workshop", cost={"Wood": 200}, hp=1_500, line_of_sight=6, build_time=40)
        self.buildings["Siege Workshop"] = siege_workshop

        university = Building(name="University", cost={"Wood": 200}, hp=2_100, line_of_sight=6, build_time=60)
        self.buildings["University"] = university

        castle = Building(name="Castle", cost={"Stone": 650}, hp=4_800, line_of_sight=11, build_time=200)
        self.buildings["Castle"] = castle

        town_center = Building(name="Town Center", cost={"Wood": 275, "Stone": 100}, hp=2_400, line_of_sight=8, build_time=100)
        self.buildings["Town Center"] = town_center

        # Imperial Age

        wonder = Building(name="Wonder", cost={"Wood": 1000, "Gold": 1000, "Stone": 1000}, hp=4_800, line_of_sight=8, build_time=3_500)
        self.buildings["Wonder"] = wonder

    # todo: code this
    def create_non_meso_civilization_units_baseline(self):
        """Allocates units available to all non-meso civilizations.

        Creates all units that are available to all the civilizations and stores them inside the buildings
        class attribute."""
        ...

    def create_teutons(self):
        """Creates the Teutons civilization.

        Equips all buildings with the units and researches available to that civ.

        Uses the civ data from data.upgrades.py, and then calls the assign_available_researches from the
        classes.Building class and passing it the data fetched.

        After that, calls the assign_available_units to do the same with Units."""

        # BUILDINGS
        self.create_non_meso_civilization_building_baseline()

        teutons_available_researches_lumber_camp = [
            "Double-Bit Axe",
            "Bow Saw",
            "Two-Man Saw",
        ]

        self.buildings["Lumber Camp"].assign_available_researches(teutons_available_researches_lumber_camp)

        teutons_available_researches_mill = [
            "Horse Collar",
            "Heavy Plow",
            "Crop Rotation",
        ]

        self.buildings["Mill"].assign_available_researches(teutons_available_researches_mill)

        teutons_available_researches_mining_camp = [
            "Gold Mining",
            "Gold Shaft Mining",
            "Stone Mining",
            "Stone Shaft Mining"
        ]

        self.buildings["Mining Camp"].assign_available_researches(teutons_available_researches_mining_camp)

        teutons_available_researches_dock = [
            "Gillnets",
            "Careening",
        ]

        self.buildings["Dock"].assign_available_researches(teutons_available_researches_dock)

        teutons_available_researches_barracks = [
            "Man-at-Arms",
            "Long Swordsman",
            "Two-Handed Swordsman",
            "Champion",
            "Pikeman",
            "Halberdier",
            "Supplies",
            "Squires",
            "Arson",
        ]

        self.buildings["Barracks"].assign_available_researches(teutons_available_researches_barracks)

        teutons_available_researches_blacksmith = [
            "Padded Archer Armor",
            "Leather Archer Armor",
            "Ring Archer Armor",
            "Fletching",
            "Bodkin Arrow",
            "Forging",
            "Iron Casting",
            "Blast Furnace",
            "Scale Barding Armor",
            "Chain Barding Armor",
            "Plate Barding Armor",
            "Scale Mail Armor",
            "Chain Mail Armor",
            "Plate Mail Armor"
        ]

        self.buildings["Blacksmith"].assign_available_researches(teutons_available_researches_blacksmith)

        teutons_available_researches_archery_range = [
            "Crossbowman",
            "Elite Skirmisher",
        ]

        self.buildings["Archery Range"].assign_available_researches(teutons_available_researches_archery_range)

        teutons_available_researches_stable = [
            "Cavalier",
            "Paladin",
            "Bloodlines"
        ]

        self.buildings["Stable"].assign_available_researches(teutons_available_researches_stable)

        # UNITS
        self.create_non_meso_civilization_units_baseline()

        teutons_available_barrack_units = [
            "Militia",
            "Man-at-Arms",
            "Long Swordsman",
            "Two-Handed Swordsman",
            "Champion",
            "Spearman",
            "Pikeman",
            "Halberdier",
        ]

        self.buildings["Barracks"].assign_available_units(teutons_available_barrack_units)
