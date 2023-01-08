"""Contains all the upgrades / research data, emulating a local database."""

upgrades_data = {

    # Barracks
    "Man-at-Arms": {
        "Name": "Man-at-Arms Upgrade",
        "Cost": {"Food": 100, "Gold": 40},
        "Explanation Text": "Allows creation of Man-at-Arms.",
        "Research Time": 40
    },

    "Long Swordsman": {
        "Name": "Long Swordsman Upgrade",
        "Cost": {"Food": 150, "Gold": 65},
        "Explanation Text": "Allows creation of Long Swordsman.",
        "Research Time": 45
    },

    "Two-Handed Swordsman": {
        "Name": "Two-Handed Swordsman",
        "Cost": {"Food": 300, "Gold": 100},
        "Explanation Text": "Allows creation of Two-Handed Swordsman.",
        "Research Time": 75
    },

    "Champion": {
        "Name": "Champion",
        "Cost": {"Food": 750, "Gold": 350},
        "Explanation Text": "Allows creation of Champion.",
        "Research Time": 100
    },

    "Pikeman": {
        "Name": "Pikeman",
        "Cost": {"Food": 215, "Gold": 90},
        "Explanation Text": "Allows creation of Pikeman.",
        "Research Time": 45
    },

    "Halberdier": {
        "Name": "Halberdier",
        "Cost": {"Food": 300, "Gold": 600},
        "Explanation Text": "Allows creation of Halberdier.",
        "Research Time": 50
    },

    "Supplies": {
        "Name": "Supplies",
        "Cost": {"Food": 100, "Gold": 40},
        "Explanation Text": "Militia-line costs -15 food.",
        "Research Time": 35

    },

    "Squires": {
        "Name": "Squires",
        "Cost": {"Food": 100},
        "Explanation Text": "Infantry move 10% faster.",
        "Research Time": 40,
    },

    "Arson": {
        "Name": "Arson",
        "Cost": {"Food": 150, "Gold": 50},
        "Explanation Text": "Infantry do more damage vs. buildings.",
        "Research Time": 25,
    },

    # Lumber Camp
    "Double-Bit Axe": {
            "Name": "Double-Bit Axe",
            "Cost": {"Food": 100, "Wood": 50},
            "Explanation Text": "Villagers chop wood 20% faster.",
            "Research Time": 25,
        },

    "Bow Saw": {
            "Name": "Bow Saw",
            "Cost": {"Food": 150, "Wood": 100},
            "Explanation Text": "Villagers chop wood 20% faster.",
            "Research Time": 50,
        },

    "Two-Man Saw": {
            "Name": "Two-Man Saw",
            "Cost": {"Food": 300, "Wood": 200},
            "Explanation Text": "Villagers chop wood 10% faster.",
            "Research Time": 100,
        },

    # Mill
    "Horse Collar": {
            "Name": "Horse Collar",
            "Cost": {"Food": 75, "Wood": 75},
            "Explanation Text": "Farms produce +75 food so they last longer before you must rebuild them.",
            "Research Time": 20,
        },

    "Heavy Plow": {
            "Name": "Heavy Plow",
            "Cost": {"Food": 125, "Wood": 125},
            "Explanation Text": "Farms produce +125 food so they last longer before you must rebuild them. Farmers carry +1 food each trip.",
            "Research Time": 40,
        },

    "Crop Rotation": {
            "Name": "Crop Rotation",
            "Cost": {"Food": 250, "Wood": 250},
            "Explanation Text": "Farms produce +175 food so they last longer before you must rebuild them.",
            "Research Time": 70,
        },

    # Mining Camp
    "Gold Mining": {
        "Name": "Gold Mining",
        "Cost": {"Food": 100, "Wood": 75},
        "Explanation Text": "Villagers mine gold 15% faster.",
        "Research Time": 30,
    },

    "Gold Shaft Mining": {
        "Name": "Gold Shaft Mining",
        "Cost": {"Food": 200, "Wood": 150},
        "Explanation Text": "Villagers mine gold 15% faster.",
        "Research Time": 75,
    },

    "Stone Mining": {
        "Name": "Stone Mining",
        "Cost": {"Food": 100, "Wood": 75},
        "Explanation Text": "Villagers mine stone 15% faster.",
        "Research Time": 30,
    },

    "Stone Shaft Mining": {
        "Name": "Stone Shaft Mining",
        "Cost": {"Food": 200, "Wood": 150},
        "Explanation Text": "Villagers mine stone 15% faster.",
        "Research Time": 75,
    },

    # Dock
    "Fire Ship": {
        "Name": "Fire Ship",
        "Cost": {"Food": 230, "Gold": 100},
        "Explanation Text": "Allows the creation of Fire Ship.",
        "Research Time": 50,
    },

    "Fast Fire Ship": {
        "Name": "Fast Fire Ship",
        "Cost": {"Wood": 280, "Gold": 250},
        "Explanation Text": "Allows the creation of Fast Fire Ship.",
        "Research Time": 50,
    },

    "War Galley": {
        "Name": "War Galley",
        "Cost": {"Food": 230, "Gold": 100},
        "Explanation Text": "Allows the creation of War Galley.",
        "Research Time": 50,
    },

    "Galleon": {
        "Name": "Galleon",
        "Cost": {"Food": 400, "Wood": 315},
        "Explanation Text": "Allows the creation of Galleon.",
        "Research Time": 65,
    },

    "Demolition Ship": {
        "Name": "Demolition Ship",
        "Cost": {"Food": 230, "Gold": 100},
        "Explanation Text": "Allows the creation of Demolition Ship.",
        "Research Time": 50,
    },

    "Heavy Demolition Ship": {
        "Name": "Heavy Demolition Ship",
        "Cost": {"Wood": 200, "Gold": 300},
        "Explanation Text": "Allows the creation of Heavy Demolition Ship.",
        "Research Time": 50,
    },

    "Elite Cannon Galleon": {
        "Name": "Elite Cannon Galleon",
        "Cost": {"Wood": 525, "Gold": 500},
        "Explanation Text": "Allows the creation of Elite Cannon Galleon.",
        "Research Time": 30,
    },

    "Gillnets": {
        "Name": "Gillnets",
        "Cost": {"Food": 150, "Wood": 200},
        "Explanation Text": "Fishing Ships gather 25% faster.",
        "Research Time": 45,
    },

    "Careening": {
        "Name": "Careening",
        "Cost": {"Food": 250, "Gold": 150},
        "Explanation Text": "Makes ships less vulnerable to missile attack with +1 pierce armor. Transport Ships carry +5 units.",
        "Research Time": 50,
    },

    "Dry Dock": {
        "Name": "Dry Dock",
        "Cost": {"Food": 600, "Gold": 400},
        "Explanation Text": "Ships move 15% faster. Transport Ships carry +10 units.",
        "Research Time": 60,
    },

    "Shipwright": {
        "Name": "Shipwright",
        "Cost": {"Food": 1000, "Gold": 300},
        "Explanation Text": "Ships cost 20% less wood; build 35% faster.",
        "Research Time": 60,
    },

    # Blacksmith
    # Archer armor upgrades
    "Padded Archer Armor": {
        "Name": "Padded Archer Armor",
        "Cost": {"Food": 100},
        "Explanation Text": "Archers and cavalry archers have +1 normal/+1 pierce armor.",
        "Research Time": 40,
    },

    "Leather Archer Armor": {
        "Name": "Leather Archer Armor",
        "Cost": {"Food": 100, "Gold": 150},
        "Explanation Text": "Archers and cavalry archers have +1 normal/+1 pierce armor.",
        "Research Time": 55,
    },

    "Ring Archer Armor": {
        "Name": "Ring Archer Armor",
        "Cost": {"Food": 250, "Gold": 250},
        "Explanation Text": "Archers and cavalry archers have +1 normal/+2 pierce armor.",
        "Research Time": 70,
    },

    # Archers, towers and town centers attack & range upgrades
    "Fletching": {
        "Name": "Fletching",
        "Cost": {"Food": 100, "Gold": 50},
        "Explanation Text": "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack.",
        "Research Time": 30,
    },

    "Bodkin Arrow": {
        "Name": "Bodkin Arrow",
        "Cost": {"Food": 200, "Gold": 100},
        "Explanation Text": "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack.",
        "Research Time": 35,
    },

    "Bracer": {
        "Name": "Bracer",
        "Cost": {"Food": 300, "Gold": 200},
        "Explanation Text": "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack.",
        "Research Time": 40,
    },

    # Infantry and Cavalry attack upgrades
    "Forging": {
        "Name": "Forging",
        "Cost": {"Food": 100},
        "Explanation Text": "Infantry and cavalry have +1 attack.",
        "Research Time": 50,
    },

    "Iron Casting": {
        "Name": "Iron Casting",
        "Cost": {"Food": 220, "Wood": 120},
        "Explanation Text": "Infantry and cavalry have +1 attack.",
        "Research Time": 75,
    },

    "Blast Furnace": {
        "Name": "Blast Furnace",
        "Cost": {"Food": 275, "Wood": 225},
        "Explanation Text": "Infantry and cavalry have +2 attack.",
        "Research Time": 100,
    },

    # Cavalry armor upgrades
    "Scale Barding Armor": {
        "Name": "Scale Barding Armor",
        "Cost": {"Food": 150},
        "Explanation Text": "Cavalry have +1 normal/+1 pierce armor.",
        "Research Time": 45,
    },

    "Chain Barding Armor": {
        "Name": "Chain Barding Armor",
        "Cost": {"Food": 250, "Gold": 150},
        "Explanation Text": "Cavalry have +1 normal/+1 pierce armor.",
        "Research Time": 60,
    },

    "Plate Barding Armor": {
        "Name": "Plate Barding Armor",
        "Cost": {"Food": 350, "Gold": 200},
        "Explanation Text": "Cavalry have +1 normal/+2 pierce armor.",
        "Research Time": 75,
    },

    # Infantry armor upgrades
    "Scale Mail Armor": {
        "Name": "Scale Mail Armor",
        "Cost": {"Food": 100},
        "Explanation Text": "Infantry have +1 normal/+1 pierce armor.",
        "Research Time": 40,
    },

    "Chain Mail Armor": {
        "Name": "Chain Mail Armor",
        "Cost": {"Food": 200, "Gold": 100},
        "Explanation Text": "Infantry have +1 normal/+1 pierce armor.",
        "Research Time": 55,
    },

    "Plate Mail Armor": {
        "Name": "Plate Mail Armor",
        "Cost": {"Food": 300, "Gold": 150},
        "Explanation Text": "Infantry have +1 normal/+2 pierce armor.",
        "Research Time": 70,
    },

    # Archery Range
    "Crossbowman": {
        "Name": "Crossbowman",
        "Cost": {"Food": 175, "Gold": 125},
        "Explanation Text": "Allows the creation of Crossbowman.",
        "Research Time": 35,
    },

    "Arbalester": {
        "Name": "Arbalester",
        "Cost": {"Food": 450, "Wood": 400},
        "Explanation Text": "Allows the creation of Arbalester.",
        "Research Time": 50,
    },

    "Elite Skirmisher": {
        "Name": "Elite Skirmisher",
        "Cost": {"Wood": 230, "Gold": 130},
        "Explanation Text": "Allows the creation of Elite Skirmisher.",
        "Research Time": 50,
    },

    "Heavy Cavalry Archer": {
        "Name": "Heavy Cavalry Archer",
        "Cost": {"Food": 900, "Gold": 500},
        "Explanation Text": "Allows the creation of Heavy Cavalry Archer.",
        "Research Time": 50,
    },


    "Thumb Ring": {
        "Name": "Thumb Ring",
        "Cost": {"Food": 300, "Wood": 250},
        "Explanation Text": "Archers fire faster and with 100% accuracy.",
        "Research Time": 45,
    },

    "Parthian Tactics": {
        "Name": "Parthian Tactics",
        "Cost": {"Food": 200, "Gold": 250},
        "Explanation Text": "Mounted Archers have +1 normal/+2 pierce armor; Cavalry Archers have +4, Unique Mounted Archers +2 attack vs. pikemen.",
        "Research Time": 65,
    },

    # Stable
    "Light Cavalry": {
        "Name": "Light Cavalry",
        "Cost": {"Food": 150, "Gold": 50},
        "Explanation Text": "Allows the creation of Light Cavalry.",
        "Research Time": 45,
    },

    "Hussar": {
        "Name": "Hussar",
        "Cost": {"Food": 500, "Gold": 600},
        "Explanation Text": "Allows the creation of Hussar.",
        "Research Time": 50,
    },

    "Heavy Camel Rider": {
        "Name": "Heavy Camel Rider",
        "Cost": {"Food": 325, "Gold": 360},
        "Explanation Text": "Allows the creation of Heavy Camel Rider.",
        "Research Time": 105,
    },

    "Cavalier": {
        "Name": "Cavalier",
        "Cost": {"Food": 300, "Gold": 300},
        "Explanation Text": "Allows the creation of Cavalier.",
        "Research Time": 100,
    },

    "Paladin": {
        "Name": "Paladin",
        "Cost": {"Food": 1_300, "Gold": 750},
        "Explanation Text": "Allows the creation of Paladin.",
        "Research Time": 170,
    },


    "Bloodlines": {
        "Name": "Bloodlines",
        "Cost": {"Food": 150, "Gold": 100},
        "Explanation Text": "Mounted units have +20 hit points.",
        "Research Time": 50,
    },

    "Husbandry": {
        "Name": "Husbandry",
        "Cost": {"Food": 150},
        "Explanation Text": "Cavalry move 10% faster.",
        "Research Time": 40,
    },

    # Siege Workshop
    "Capped Ram": {
        "Name": "Capped Ram upgrade",
        "Cost": {"Food": 300},
        "Explanation Text": "Allows creation of Capped Ram.",
        "Research Time": 40,
    },

    "Siege Ram": {
        "Name": "Siege Ram",
        "Cost": {"Food": 1_000},
        "Explanation Text": "Allows creation of Siege Ram.",
        "Research Time": 75,
    },

    "Onager": {
        "Name": "Onager upgrade",
        "Cost": {"Food": 800, "Gold": 500},
        "Explanation Text": "Allows creation of Onager.",
        "Research Time": 75,
    },

    "Siege Onager": {
        "Name": "Siege Onager upgrade",
        "Cost": {"Food": 1_450, "Gold": 1_000},
        "Explanation Text": "Allows creation of Siege Onager.",
        "Research Time": 150,
    },

    "Heavy Scorpion": {
        "Name": "Heavy Scorpion",
        "Cost": {"Food": 1_000, "Wood": 1_100},
        "Explanation Text": "Allows creation of Heavy Scorpion.",
        "Research Time": 50,
    },

    # Castle
    "Hoardings": {
        "Name": "Hoardings",
        "Cost": {"Food": 400, "Wood": 400},
        "Explanation Text": "Strengthens Castles by providing +20% hit points.",
        "Research Time": 75,
    },

    "Sappers": {
        "Name": "Sappers",
        "Cost": {"Food": 400, "Gold": 200},
        "Explanation Text": "Villagers cause +15 damage when attacking buildings.",
        "Research Time": 10,
    },

    "Conscription": {
        "Name": "Conscription",
        "Cost": {"Food": 150, "Gold": 150},
        "Explanation Text": "Military buildings (except Siege Workshops) work 33% faster.",
        "Research Time": 60,
    },

    # Town Center
    "Loom": {
        "Name": "Loom",
        "Cost": {"Gold": 50},
        "Explanation Text": "Makes your villagers harder to kill by providing +15 hit points and +1 normal/+2 pierce armor.",
        "Research Time": 25,
    },

    "Wheelbarrow": {
        "Name": "Wheelbarrow",
        "Cost": {"Food": 175, "Wood": 50},
        "Explanation Text": "Villagers work more efficiently by moving 10% faster and carrying 25% more resources.",
        "Research Time": 75,
    },

    "Hand Cart": {
        "Name": "Hand Cart",
        "Cost": {"Food": 300, "Wood": 200},
        "Explanation Text": "Villagers work more efficiently by moving 10% faster and carrying 50% more resources.",
        "Research Time": 55,
    },

    "Town Watch": {
        "Name": "Town Watch",
        "Cost": {"Food": 75},
        "Explanation Text": "Increases the line of sight of all buildings by +4 so they see enemies from a longer distance.",
        "Research Time": 25,
    },

    "Town Patrol": {
        "Name": "Town Patrol",
        "Cost": {"Food": 300, "Gold": 100},
        "Explanation Text": "Increases the line of sight of all buildings by +4 so they see enemies from a longer distance.",
        "Research Time": 40,
    },

    # Monastery
    "Redemption": {
        "Name": "Redemption",
        "Cost": {"Gold": 475},
        "Explanation Text": "Monks can convert enemy buildings (except Town Centers, Castles, Monasteries, Farms, Fish Traps, walls, Gates, and Wonders) and siege weapons. Monks can convert most enemy units from a distance, but they must stand adjacent to buildings, rams, and Trebuchets to convert them.",
        "Research Time": 50,
    },

    "Atonement": {
        "Name": "Atonement",
        "Cost": {"Gold": 325},
        "Explanation Text": "Monks can convert enemy Monks.",
        "Research Time": 40,
    },

    "Herbal Medicine": {
        "Name": "Herbal Medicine",
        "Cost": {"Gold": 200},
        "Explanation Text": "Units garrisoned in buildings heal 6X faster.",
        "Research Time": 35,
    },

    "Heresy": {
        "Name": "Heresy",
        "Cost": {"Gold": 1_000},
        "Explanation Text": "Units converted by an enemy Monk (or Missionary) die instead of changing to the enemy's color.",
        "Research Time": 60,
    },

    "Sanctity": {
        "Name": "Sanctity",
        "Cost": {"Gold": 120},
        "Explanation Text": "Monks have +15 hit points so they are harder to kill.",
        "Research Time": 60,
    },

    "Fervor": {
        "Name": "Fervor",
        "Cost": {"Gold": 140},
        "Explanation Text": "Monks move 15% faster.",
        "Research Time": 50,
    },

    "Faith": {
        "Name": "Faith",
        "Cost": {"Food": 750, "Gold": 1_000},
        "Explanation Text": "Units are 50% harder for enemy Monks to convert.",
        "Research Time": 60,
    },

    "Illumination": {
        "Name": "Illumination",
        "Cost": {"Gold": 120},
        "Explanation Text": "Monks regain their faith 50% faster after a successful conversion.",
        "Research Time": 65,
    },

    "Block Printing": {
        "Name": "Block Printing",
        "Cost": {"Gold": 200},
        "Explanation Text": "Monks have +3 conversion range.""Monks have +3 conversion range.",
        "Research Time": 55,
    },

    "Theocracy": {
        "Name": "Theocracy",
        "Cost": {"Gold": 200},
        "Explanation Text": "If a group of Monks converts an enemy unit, only one of the Monks must rest afterward.",
        "Research Time": 75,
    },

    # Market
    # Tribute Fees
    "Coinage": {
        "Name": "Coinage",
        "Cost": {"Food": 200, "Gold": 100},
        "Explanation Text": "Reduces fee for tributes to 20%.",
        "Research Time": 70,
    },

    "Banking": {
        "Name": "Banking",
        "Cost": {"Food": 300, "Gold": 200},
        "Explanation Text": "Tributes are free.",
        "Research Time": 70,
    },

    # Trade Cart upgrades
    "Caravan": {
        "Name": "Caravan",
        "Cost": {"Food": 200, "Gold": 200},
        "Explanation Text": "Trade Carts and Trade Cogs move 50% faster (so gold accumulates faster).",
        "Research Time": 40,
    },

    # Trading Fees
    "Guilds": {
        "Name": "Guilds",
        "Cost": {"Food": 300, "Gold": 200},
        "Explanation Text": "Reduces the commodity trading fee to 15%.",
        "Research Time": 50,
    },

    # University
    # Building HP upgrades
    "Masonry": {
        "Name": "Masonry",
        "Cost": {"Food": 150, "Wood": 175},
        "Explanation Text": "Strengthens all buildings by providing 10% more hit points, +1 normal/+1 pierce armor, and +3 building armor.",
        "Research Time": 70,
    },

    "Architecture": {
        "Name": "Architecture",
        "Cost": {"Food": 300, "Wood": 200},
        "Explanation Text": "Strengthens all buildings by providing 10% more hit points, +1 normal/+1 pierce armor, and +3 building armor.",
        "Research Time": 70,
    },

    "Fortified Wall": {
        "Name": "Fortified Wall",
        "Cost": {"Food": 200, "Wood": 100},
        "Explanation Text": "Upgrades your Stone Walls and lets you build Fortified Walls, which are stronger and harder to breach. Also increases the hit points of your Gates, which makes them harder to destroy.",
        "Research Time": 50,
    },

    # Tower upgrades
    "Guard Tower": {
        "Name": "Guard Tower",
        "Cost": {"Food": 100, "Wood": 250},
        "Explanation Text": "Upgrades your Watch Towers and lets you build Guard Towers, which are stronger and have more attack strength.",
        "Research Time": 30,
    },

    "Keep": {
        "Name": "Keep",
        "Cost": {"Food": 500, "Wood": 350},
        "Explanation Text": "Upgrades Guard Towers and lets you build Keeps, which are stronger and have more attack strength, range, and armor.",
        "Research Time": 75,
    },

    "Treadmill Crane": {
        "Name": "Treadmill Crane",
        "Cost": {"Food": 300, "Wood": 200},
        "Explanation Text": "Villagers construct buildings 20% faster.",
        "Research Time": 50,
    },

    "Murder Holes": {
        "Name": "Murder Holes",
        "Cost": {"Food": 200, "Stone": 100},
        "Explanation Text": "Eliminates the minimum range of all towers, Castles and Harbors so they can fire at enemies attacking their base.",
        "Research Time": 60,
    },

    "Ballistics": {
        "Name": "Ballistics",
        "Cost": {"Wood": 300, "Gold": 175},
        "Explanation Text": "Archers, Town Centers, Castles, Galleys, Unique Naval Units, and Mounted Archers fire more accurately at moving targets.",
        "Research Time": 60,
    },

    "Chemistry": {
        "Name": "Chemistry",
        "Cost": {"Food": 300, "Gold": 200},
        "Explanation Text": "Missile units (except gunpowder units) have +1 attack strength.",
        "Research Time": 100,
    },

    "Siege Engineers": {
        "Name": "Siege Engineers",
        "Cost": {"Food": 500, "Wood": 600},
        "Explanation Text": "Siege weapons have +1 range (except rams and Armored Elephants) and cause 20% more damage to buildings (40% more for Petards).",
        "Research Time": 45,
    },

    "Arrowslits": {
        "Name": "Arrowslits",
        "Cost": {"Food": 250, "Wood": 250},
        "Explanation Text": "Increases the attack of towers and Donjons.",
        "Research Time": 25,
    },

    "Bombard Tower": {
        "Name": "Bombard Tower",
        "Cost": {"Food": 800, "Wood": 400},
        "Explanation Text": "Lets you build Bombard Towers, which are powerful and have extensive line of sight.",
        "Research Time": 60,
    },

    "Heated Shot": {
        "Name": "Heated Shot",
        "Cost": {"Food": 350, "Gold": 100},
        "Explanation Text": "Towers cause 125% more damage to ships; Castles cause 25% more damage to ships.",
        "Research Time": 30,
    },
}


unique_techs = {

    "Teutons": {

        "Elite Teutonic Knight": {
            "Name": "Elite Teutonic Knight upgrade",
            "Cost": {"Food": 950, "Gold": 500},
            "Explanation Text": "Allows the creation of Elite Teutonic Knight.",
            "Research Time": 50,
        },

        "Ironclad": {
            "Name": "Ironclad",
            "Cost": {"Wood": 400, "Gold": 350},
            "Explanation Text": "Increases the armor of all siege weapons so they're more resistant to melee attack.",
            "Research Time": 60,
        },

        "Crenellations": {
            "Name": "Crenellations",
            "Cost": {"Food": 600, "Stone": 400},
            "Explanation Text": "Castles have +3 range; garrisoned infantry fire arrows.",
            "Research Time": 60,
        },
    },

    "Mongols": {

        "Elite Mangudai": {
            "Name": "Elite Mangudai upgrade",
            "Cost": {"Food": 1_100, "Gold": 675},
            "Explanation Text": "Allows the creation of Elite Mangudai.",
            "Research Time": 50,
        },

        "Nomads": {
            "Name": "Nomads",
            "Cost": {"Wood": 300, "Gold": 150},
            "Explanation Text": "Houses don't lose their population room when they are destroyed.",
            "Research Time": 40,
        },

        "Drill": {
            "Name": "Drill",
            "Cost": {"Wood": 500, "Gold": 450},
            "Explanation Text": "Siege Workshop units move 50% faster.",
            "Research Time": 60,
        },
    },

    "Goths": {

        "Elite Huskarl": {
            "Name": "Elite Huskarl upgrade",
            "Cost": {"Food": 1_200, "Gold": 550},
            "Explanation Text": "Allows the creation of Elite Huskarl.",
            "Research Time": 40,
        },

        "Anarchy": {
            "Name": "Anarchy",
            "Cost": {"Food": 450, "Gold": 250},
            "Explanation Text": "Allows Huskarls to be created at the Barracks.",
            "Research Time": 40,
        },

        "Perfusion": {
            "Name": "Perfusion",
            "Cost": {"Wood": 400, "Gold": 600},
            "Explanation Text": "Barracks units are created 100% faster.",
            "Research Time": 40,
        },
    },

    "Franks": {

        "Elite Throwing Axeman": {
            "Name": "Elite Throwing Axeman upgrade",
            "Cost": {"Food": 1_000, "Gold": 750},
            "Explanation Text": "Allows the creation of Elite Throwing Axeman.",
            "Research Time": 45,
        },

        "Bearded Axe": {
            "Name": "Bearded Axe",
            "Cost": {"Food": 300, "Gold": 300},
            "Explanation Text": "Throwing Axemen have +1 range.",
            "Research Time": 60,
        },

        "Chivalry": {
            "Name": "Chivalry",
            "Cost": {"Wood": 600, "Gold": 500},
            "Explanation Text": "Increases the production speed of stables by +40%.",
            "Research Time": 60,
        },
    },

    "Britons": {

        "Elite Longbowman": {
            "Name": "Elite Longbowman upgrade",
            "Cost": {"Food": 850, "Gold": 850},
            "Explanation Text": "Allows the creation of Elite Longbowman.",
            "Research Time": 60,
        },

        "Yeomen": {
            "Name": "Yeomen",
            "Cost": {"Wood": 750, "Gold": 450},
            "Explanation Text": "Foot archers have +1 range; towers have +2 attack.",
            "Research Time": 60,
        },

        "Warwolf": {
            "Name": "Warwolf",
            "Cost": {"Wood": 800, "Gold": 400},
            "Explanation Text": "Improves your Trebuchets by giving them blast damage.",
            "Research Time": 40,
        },
    },

    "Byzantines": {

        "Elite Cataphract": {
            "Name": "Elite Cataphract upgrade",
            "Cost": {"Food": 1_200, "Gold": 800},
            "Explanation Text": "Allows the creation of Elite Cataphract.",
            "Research Time": 50,
        },

        "Greek Fire": {
            "Name": "Greek Fire",
            "Cost": {"Food": 250, "Gold": 300},
            "Explanation Text": "Fire Ships have +1 range.",
            "Research Time": 40,
        },

        "Logistica": {
            "Name": "Logistica",
            "Cost": {"Food": 800, "Gold": 600},
            "Explanation Text": "Cataphracts cause trample damage.",
            "Research Time": 50,
        },
    },

    "Celts": {

        "Elite Woad Raider": {
            "Name": "Elite Woad Raider upgrade",
            "Cost": {"Food": 1_000, "Gold": 800},
            "Explanation Text": "Allows the creation of Elite Woad Raider.",
            "Research Time": 45,
        },

        "Stronghold": {
            "Name": "Stronghold",
            "Cost": {"Food": 250, "Gold": 200},
            "Explanation Text": "Makes your castles and towers stronger by making them fire 25% faster.",
            "Research Time": 30,
        },

        "Furor Celtica": {
            "Name": "Furor Celtica",
            "Cost": {"Food": 750, "Gold": 450},
            "Explanation Text": "Siege Workshop units have +40% hit points.",
            "Research Time": 50,
        },
    },
}
