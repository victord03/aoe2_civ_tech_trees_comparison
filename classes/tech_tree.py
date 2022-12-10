class TechTree:

    empty_tech_tree = {
        "Barracks": {
            "Militia": bool,
            "Man-at-Arms": bool,
            "Long Swordsman": bool,
            "Two-Handed Swordsman": bool,
            "Champion": bool,
            "Spearman": bool,
            "Pikeman": bool,
            "Halberdier": bool,
            "Eagle Scout": bool,
            "Eagle Warrior": bool,
            "Elite Eagle warrior": bool,
            "Supplies": bool,
            "Squires": bool,
            "Arson": bool,
        },
        "Archery Range": {
            "Archer": bool,
            "Crossbowman": bool,
            "Arbalester": bool,
            "Skirmisher": bool,
            "Elite Skirmisher": bool,
            "Cavalry Archer": bool,
            "Heavy Cavalry Archer": bool,
            "Hand Cannoneer": bool,
            "Thumb Ring": bool,
            "Parthian Tactics": bool,
        },
        "Stables": {
            "Scout Cavalry": bool,
            "Light Cavalry": bool,
            "Hussar": bool,
            "Knight": bool,
            "Cavalier": bool,
            "Paladin": bool,
            "Camel Rider": bool,
            "Heavy Camel Rider": bool,
            "Bloodlines": bool,
            "Husbandry": bool,
        },
        "Blacksmith": {
            "Padded Archer Armor": bool,
            "Leather Archer Armor": bool,
            "Ring Archer Armor": bool,
            "Fletching": bool,
            "Bodkin Arrow": bool,
            "Bracer": bool,
            "Forging": bool,
            "Iron Casting": bool,
            "Blast Furnace": bool,
            "Scale Barding Armor": bool,
            "Chain Barding Armor": bool,
            "Plate Barding Armor": bool,
            "Scale Mail Armor": bool,
            "Chain Mail Armor": bool,
            "Plate Mail Armor": bool,
        },
        "Siege Workshop": {
            "Battering Ram": bool,
            "Capped Ram": bool,
            "Siege Ram": bool,
            "Mangonel": bool,
            "Onager": bool,
            "Siege Onager": bool,
            "Scorpion": bool,
            "Heavy Scorpion": bool,
            "Bombard Cannon": bool,
            "Siege Tower": bool,
        },
        "Dock": {
            "Fishing Ship": bool,
            "Transport Ship": bool,
            "Fire Galley": bool,
            "Fire Ship": bool,
            "Fast Fire Ship": bool,
            "Trade Cog": bool,
            "Demolition Raft": bool,
            "Demolition Ship": bool,
            "Heavy Demolition Ship": bool,
            "Galley": bool,
            "War Galley": bool,
            "Galleon": bool,
            "Cannon Galleon": bool,
            "Elite Cannon Galleon": bool,
            "Gillnets": bool,
            "careening": bool,
            "Dry Dock": bool,
            "Shipwright": bool,
        },
        "University": {
            "Masonry": bool,
            "Architecture": bool,
            "Fortified Wall": bool,
            "Guard Tower": bool,
            "Keep": bool,
            "Arrowslits": bool,
            "Murder Holes": bool,
            "Treadmill Crane": bool,
            "Chemistry": bool,
            "Ballistics": bool,
            "Bombard Tower": bool,
            "Heated Shot": bool,
            "Siege Engineers": bool,
        },
        "Stone Wall": {
            "Available": bool,
        },
        "Castle": {
            "Hoardings": bool,
            "Sappers": bool,
            "Conscription": bool,
        },
        "Monastery": {
            "Redemption": bool,
            "Atonement": bool,
            "Herbal Medicine": bool,
            "Heresy": bool,
            "Sanctity": bool,
            "Fervor": bool,
            "Faith": bool,
            "Illumination": bool,
            "Block Printing": bool,
            "Theocracy": bool,
        },
        "Town Center": {
            "Loom": bool,
            "Town Watch": bool,
            "Town Patrol": bool,
            "Wheelbarrow": bool,
            "Hand Cart": bool,
        },
        "Mining Camp": {
            "Gold Mining": bool,
            "Gold Shaft Mining": bool,
            "Stone Mining": bool,
            "Stone Shaft Mining": bool,
        },
        "Lumber Camp": {
            "Double-Bit Axe": bool,
            "Bow Saw": bool,
            "Two-Man Saw": bool,
        },
        "Market": {
            "Coinage": bool,
            "Banking": bool,
            "Caravan": bool,
            "Guilds": bool,
        },
        "Mill": {
            "Horse Collar": bool,
            "Heavy Plow": bool,
            "Crop Rotation": bool,
        },
    }

    civ_tree: dict

    def __init__(self, not_available_techs: list):

        self.civ_tree = self.empty_tech_tree.copy()

        for key, value in self.empty_tech_tree.items():
            for inner_key in value:

                if inner_key in not_available_techs:
                    self.civ_tree[key][inner_key] = False
                else:
                    self.civ_tree[key][inner_key] = True