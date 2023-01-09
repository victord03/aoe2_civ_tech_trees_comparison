from classes.Building import Building
from data.units import units as unit_data


class Civilization:

    bonus: dict[str: int]
    buildings: dict
    age: str

    def __init__(self):
        """Init method for the Civilization class.

        Initiates the attributes bonus and buildings as empty dicts."""
        self.bonus = dict()
        self.buildings = dict()
        self.age = "Dark Age"

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

    def create_non_meso_civilization_research_baseline(self):
        """Allocates research available to all non-meso civilizations.

        Creates all researches that are available to all the civilizations and stores them inside the buildings
        class attribute."""

        # Town Center
        town_center = [
            "Loom",
            "Wheelbarrow",
            "Town Watch",
        ]
        self.buildings["Town Center"].assign_available_researches = town_center

        # Lumber Camp
        lumber_camp = [
            "Double-Bit Axe",
        ]
        self.buildings["Lumber Camp"].assign_available_researches = lumber_camp

        # Mill
        mill = [
            "Horse Collar",
        ]
        self.buildings["Mill"].assign_available_researches = mill

        # Mining Camp
        mining_camp = [
            "Gold Mining",
            "Stone Mining",
        ]
        self.buildings["Mining Camp"].assign_available_researches = mining_camp

        # Dock
        dock = [
            "Fire Ship",
            "War Galley",
            "Demolition Ship",
        ]
        self.buildings["Dock"].assign_available_researches = dock

        # Blacksmith
        blacksmith = [
            "Padded Archer Armor",
            "Fletching",
            "Forging",
            "Scale Barding Armor",
            "Scale Mail Armor"
        ]
        self.buildings["Blacksmith"].assign_available_researches = blacksmith

        # Market
        market = [
            "Coinage",
            "Caravan",
        ]
        self.buildings["Market"].assign_available_researches = market

        # Barracks
        barracks = [
            "Man-at-Arms",
            "Long Swordsman",
            "Two-Handed Swordsman",
            "Pikeman",
        ]
        self.buildings["Barracks"].assign_available_researches = barracks

        # Archery Range
        archery_range = [
            "Crossbowman",
        ]
        self.buildings["Archery Range"].assign_available_researches = archery_range

        # Stable
        stable = [
            "Cavalier",
        ]
        self.buildings["Stable"].assign_available_researches = stable

    def create_non_meso_civilization_units_baseline(self):
        """Allocates units available to all non-meso civilizations.

        Creates all units that are available to all the civilizations and stores them inside the buildings
        class attribute."""

        # Town Center
        self.buildings["Town Center"].available_units = unit_data["Villager"]

        # Dock
        self.buildings["Dock"].available_units = unit_data["Fishing Ship"]
        self.buildings["Dock"].available_units = unit_data["Transport Ship"]
        self.buildings["Dock"].available_units = unit_data["Trade Cog"]
        self.buildings["Dock"].available_units = unit_data["Fish Trap"]
        self.buildings["Dock"].available_units = unit_data["Fire Galley"]
        self.buildings["Dock"].available_units = unit_data["Demolition Raft"]
        self.buildings["Dock"].available_units = unit_data["Galley"]

        # Market
        self.buildings["Market"].available_units = unit_data["Trade Cart"]

        # Barracks
        self.buildings["Barracks"].available_units = unit_data["Militia"]
        self.buildings["Barracks"].available_units = unit_data["Man-at-Arms"]
        self.buildings["Barracks"].available_units = unit_data["Long Swordsman"]
        self.buildings["Barracks"].available_units = unit_data["Two-Handed Swordsman"]
        self.buildings["Barracks"].available_units = unit_data["Spearman"]
        self.buildings["Barracks"].available_units = unit_data["Pikeman"]

        # Archery Range
        self.buildings["Archery Range"].available_units = unit_data["Archer"]
        self.buildings["Archery Range"].available_units = unit_data["Crossbowman"]
        self.buildings["Archery Range"].available_units = unit_data["Skirmisher"]
        self.buildings["Archery Range"].available_units = unit_data["Cavalry Archer"]

        # Stable
        self.buildings["Stable"].available_units = unit_data["Scout Cavalry"]
        self.buildings["Stable"].available_units = unit_data["Knight"]

        # Siege Workshop
        self.buildings["Siege Workshop"].available_units = unit_data["Battering Ram"]
        self.buildings["Siege Workshop"].available_units = unit_data["Mangonel"]
        self.buildings["Siege Workshop"].available_units = unit_data["Scorpion"]
        self.buildings["Siege Workshop"].available_units = unit_data["Siege Tower"]

        # Castle
        self.buildings["Castle"].available_units = unit_data["Petard"]
        self.buildings["Castle"].available_units = unit_data["Trebuchet"]

        # Monastery
        self.buildings["Monastery"].available_units = unit_data["Monk"]

    def create_teutons(self):
        """Creates the Teutons civilization.

        Equips all buildings with the units and researches available to that civ.

        Uses the civ data from data.upgrades.py, and then calls the assign_available_researches from the
        classes.Building class and passing it the data fetched.

        After that, calls the assign_available_units to do the same with Units."""

        #### BUILDINGS
        self.create_non_meso_civilization_building_baseline()



        #### TECHS
        self.create_non_meso_civilization_research_baseline()

        # Town Center
        teutons_available_researches_town_center = [
            "Hand Cart",
            "Town Patrol",
        ]
        self.buildings["Town Center"].assign_available_researches(teutons_available_researches_town_center)

        teutons_available_researches_lumber_camp = [
            "Bow Saw",
            "Two-Man Saw",
        ]

        self.buildings["Lumber Camp"].assign_available_researches(teutons_available_researches_lumber_camp)

        teutons_available_researches_mill = [
            "Heavy Plow",
            "Crop Rotation",
        ]

        self.buildings["Mill"].assign_available_researches(teutons_available_researches_mill)

        teutons_available_researches_mining_camp = [
            "Gold Shaft Mining",
            "Stone Shaft Mining"
        ]

        self.buildings["Mining Camp"].assign_available_researches(teutons_available_researches_mining_camp)

        teutons_available_researches_dock = [
            "Gillnets",
            "Careening",
        ]

        self.buildings["Dock"].assign_available_researches(teutons_available_researches_dock)

        # Market
        teutons_available_researches_market = [
            "Banking",
            "Guilds",
        ]
        self.buildings["Market"].assign_available_researches(teutons_available_researches_market)

        teutons_available_researches_barracks = [
            "Champion",
            "Halberdier",
            "Supplies",
            "Squires",
            "Arson",
        ]

        self.buildings["Barracks"].assign_available_researches(teutons_available_researches_barracks)

        teutons_available_researches_blacksmith = [
            "Leather Archer Armor",
            "Ring Archer Armor",
            "Bodkin Arrow",
            "Iron Casting",
            "Blast Furnace",
            "Chain Barding Armor",
            "Plate Barding Armor",
            "Chain Mail Armor",
            "Plate Mail Armor"
        ]

        self.buildings["Blacksmith"].assign_available_researches(teutons_available_researches_blacksmith)

        teutons_available_researches_archery_range = [
            "Elite Skirmisher",
        ]

        self.buildings["Archery Range"].assign_available_researches(teutons_available_researches_archery_range)

        teutons_available_researches_stable = [
            "Paladin",
            "Bloodlines"
        ]

        self.buildings["Stable"].assign_available_researches(teutons_available_researches_stable)

        # Siege Workshop
        teutons_available_researches_siege_workshop = [
            "Capped Ram",
            "Onager",
            "Siege Onager",
            "Heavy Scorpion",
        ]
        self.buildings["Siege Workshop"].assign_available_researches(teutons_available_researches_siege_workshop)

        # Dock
        teutons_available_researches_dock = [
            "Fire Ship",
            "Fast Fire Ship",
            "War Galley",
            "Galleon",
            "Demolition Ship",
            "Heavy Demolition Ship",
            "Gillnets",
            "Careening",
        ]
        self.buildings["Dock"].assign_available_researches(teutons_available_researches_dock)

        # Castle
        teutons_available_researches_castle = [
            "Elite Teutonic Knight",
            "Ironclad",
            "Crenellations",
        ]
        self.buildings["Castle"].assign_available_researches(teutons_available_researches_castle)

        # Monastery
        teutons_available_researches_monastery = [
            "Redemption",
            "Atonement",
            "Herbal Medicine",
            "Heresy",
            "Sanctity",
            "Fervor",
            "Faith",
            "Illumination",
            "Block Printing",
            "Theocracy",
        ]
        self.buildings["Monastery"].assign_available_researches(teutons_available_researches_monastery)

        # University
        teutons_available_researches_university = [
            "Masonry",
            "Fortified Wall",
            "Guard Tower",
            "Keep",
            "Murder Holes",
            "Ballistics",
            "Chemistry",
            "Siege Engineers",
            "Arrowslits",
            "Bombard Tower",
            "Heated Shot"
        ]
        self.buildings["University"].assign_available_researches(teutons_available_researches_university)



        #### UNITS
        self.create_non_meso_civilization_units_baseline()

        # Dock
        teutons_available_dock_units = [
            "Fire Ship",
            "Fast Fire Ship",
            "Demolition Ship",
            "Heavy Demolition Ship",
            "War Galley",
            "Galleon",
            "Cannon Galleon",
        ]
        self.buildings["Dock"].assign_available_units(teutons_available_dock_units)

        # Barracks
        teutons_available_barrack_units = [
            "Champion",
            "Halberdier",
        ]
        self.buildings["Barracks"].assign_available_units(teutons_available_barrack_units)

        # Archery Range
        teutons_available_archery_range_units = [
            "Elite Skirmisher",
            "Hand Cannoneer",
        ]
        self.buildings["Archery Range"].assign_available_units(teutons_available_archery_range_units)

        # Stable
        teutons_available_stable_units = [
            "Paladin"
        ]
        self.buildings["Stable"].assign_available_units(teutons_available_stable_units)

        # Siege Workshop
        teutons_available_siege_workshop_units = [
            "Capped Ram",
            "Onager",
            "Siege Onager",
            "Heavy Scorpion",
            "Bombard Cannon",
            "Siege Tower"
        ]
        self.buildings["Siege Workshop"].assign_available_units(teutons_available_siege_workshop_units)

        # Castle
        teutons_available_castle_units = [
            "Teutonic Knight",
            "Elite Teutonic Knight",
        ]
        self.buildings["Castle"].assign_available_units(teutons_available_castle_units)
