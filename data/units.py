"""Contains all the unit data, emulating a local database."""


# todo: 'Garrison' and 'Minimum Range' need to be added to all units

units = {
    # Town Center
    "Villager": {
        "Name": "Villager",
        "Cost": {"Food": 50},
        "HP": 25,
        "Attack": 3,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 4,
        "Garrison": 0,
        "Explanation Text": "Gathers resources. Builds and repairs buildings. Also repairs ships and siege weapons.",
        "Build Time": 25
    },

    # Dock
    "Fishing Ship": {
        "Name": "Fishing Ship",
        "Cost": {"Wood": 75},
        "HP": 60,
        "Attack": 0,
        "Armor": 0,
        "Pierce Armor": 4,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 5,
        "Garrison": 0,
        "Explanation Text": "Gathers food from fish and Fish Traps. Builds Fish Traps.",
        "Build Time": 40
    },

    "Transport Ship": {
        "Name": "Transport Ship",
        "Cost": {"Wood": 125},
        "HP": 100,
        "Attack": 0,
        "Armor": 4,
        "Pierce Armor": 8,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 5,
        "Garrison": 5,
        "Explanation Text": "Used to move units across water.",
        "Build Time": 46
    },

    "Trade Cog": {
        "Name": "Trade Cog",
        "Cost": {"Wood": 100, "Gold": 50},
        "HP": 80,
        "Attack": 0,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 6,
        "Garrison": 0,
        "Explanation Text": "Trade unit used for generating gold at another player's Dock.",
        "Build Time": 36
    },

    "Fish Trap": {
        "Name": "Fish Trap",
        "Cost": {"Wood": 100},
        "HP": 50,
        "Attack": 0,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 1,
        "Garrison": 0,
        "Explanation Text": "Renewable food source, similar to a farm but built by Fishing Ships.",
        "Build Time": 40
    },

    "Fire Galley": {
        "Name": "Fire Galley",
        "Cost": {"Wood": 75, "Gold": 45},
        "HP": 100,
        "Attack": 1,
        "Armor": 0,
        "Pierce Armor": 4,
        "Range": 2.5,
        "Minimum Range": 0,
        "Line of Sight": 1,
        "Garrison": 0,
        "Explanation Text": "Warship that spews fire at close range. Strong vs. Galleys. Weak vs. Demolition Rafts.",
        "Build Time": 65
    },

    "Fire Ship": {
        "Name": "Fire Ship",
        "Cost": {"Wood": 75, "Gold": 45},
        "HP": 120,
        "Attack": 2,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 2.5,
        "Minimum Range": 0,
        "Line of Sight": 5,
        "Garrison": 0,
        "Explanation Text": "Warship that spews fire at close range. Strong vs. War Galleys. Weak vs. Demolition Ships.",
        "Build Time": 36
    },

    "Fast Fire Ship": {
        "Name": "Fast Fire Ship",
        "Cost": {"Wood": 75, "Gold": 45},
        "HP": 140,
        "Attack": 3,
        "Armor": 0,
        "Pierce Armor": 8,
        "Range": 2.5,
        "Minimum Range": 0,
        "Line of Sight": 6,
        "Garrison": 0,
        "Explanation Text": "Warship that spews fire at close range. Strong vs. War Galleys. Weak vs. Demolition Ships.",
        "Build Time": 36
    },

    "Demolition Raft": {
        "Name": "Demolition Raft",
        "Cost": {"Wood": 70, "Gold": 50},
        "HP": 45,
        "Attack": 90,
        "Armor": 0,
        "Pierce Armor": 2,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 6,
        "Garrison": 0,
        "Explanation Text": "Demolition ship armed with explosives. Strong vs. Fire Galleys and buildings. Self-destructs when used.",
        "Build Time": 45
    },

    "Demolition Ship": {
        "Name": "Demolition Ship",
        "Cost": {"Wood": 70, "Gold": 50},
        "HP": 60,
        "Attack": 110,
        "Armor": 0,
        "Pierce Armor": 3,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 6,
        "Garrison": 0,
        "Explanation Text": "Demolition ship armed with explosives. Strong vs. Fire Ships and buildings. Self-destructs when used.",
        "Build Time": 31
    },

    "Heavy Demolition Ship": {
        "Name": "Heavy Demolition Ship",
        "Cost": {"Wood": 70, "Gold": 50},
        "HP": 70,
        "Attack": 140,
        "Armor": 0,
        "Pierce Armor": 5,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 6,
        "Garrison": 0,
        "Explanation Text": "Demolition ship armed with explosives. Strong vs. Fire Ships and buildings. Self-destructs when used.",
        "Build Time": 31
    },

    "Galley": {
        "Name": "Galley",
        "Cost": {"Wood": 90, "Gold": 30},
        "HP": 120,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 5,
        "Minimum Range": 0,
        "Line of Sight": 7,
        "Garrison": 0,
        "Explanation Text": "All-purpose warship with ranged attack. Weak vs. Fire Galleys.",
        "Build Time": 60
    },

    "War Galley": {
        "Name": "War Galley",
        "Cost": {"Wood": 90, "Gold": 30},
        "HP": 135,
        "Attack": 7,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 6,
        "Minimum Range": 0,
        "Line of Sight": 8,
        "Garrison": 0,
        "Explanation Text": "All-purpose warship with ranged attack. Weak vs. Fire Ships.",
        "Build Time": 36
    },

    "Galleon": {
        "Name": "Galleon",
        "Cost": {"Wood": 90, "Gold": 30},
        "HP": 165,
        "Attack": 8,
        "Armor": 0,
        "Pierce Armor": 8,
        "Range": 7,
        "Minimum Range": 0,
        "Line of Sight": 9,
        "Garrison": 0,
        "Explanation Text": "All-purpose warship with ranged attack. Weak vs. Fire Ships.",
        "Build Time": 36
    },

    "Cannon Galleon": {
        "Name": "Cannon Galleon",
        "Cost": {"Wood": 200, "Gold": 150},
        "HP": 120,
        "Attack": 35,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 13,
        "Minimum Range": 3,
        "Line of Sight": 15,
        "Garrison": 0,
        "Explanation Text": "Anti-building siege warship with long range, but cannot attack enemies at close range. Strong vs. buildings. Weak vs. other units.",
        "Build Time": 46
    },

    "Elite Cannon Galleon": {
        "Name": "Elite Cannon Galleon",
        "Cost": {"Wood": 200, "Gold": 150},
        "HP": 150,
        "Attack": 45,
        "Armor": 0,
        "Pierce Armor": 8,
        "Range": 15,
        "Minimum Range": 3,
        "Line of Sight": 17,
        "Garrison": 0,
        "Explanation Text": "Anti-building siege warship with long range, but cannot attack enemies at close range. Strong vs. buildings. Weak vs. other units.",
        "Build Time": 46
    },

    # Market
    "Trade Cart": {
        "Name": "Trade Cart",
        "Cost": {"Wood": 100, "Gold": 50},
        "HP": 70,
        "Attack": 0,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 7,
        "Garrison": 0,
        "Explanation Text": "Trade unit used for generating gold at another player's Market.",
        "Build Time": 51
    },

    # Barracks
    "Militia": {
        "Name": "Militia",
        "Cost": {"Food": 60, "Gold": 20},
        "HP": 40,
        "Attack": 4,
        "Armor": 0,
        "Pierce Armor": 1,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "All-purpose infantry unit. Strong vs. buildings and infantry. Weak vs. archers at long range.",
        "Build Time": 21
    },

    "Man-at-Arms": {
        "Name": "Man-at-Arms",
        "Cost": {"Food": 60, "Gold": 20},
        "HP": 45,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 1,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "All-purpose infantry unit. Strong vs. buildings and infantry. Weak vs. archers at long range.",
        "Build Time": 21
    },

    "Long Swordsman": {
        "Name": "Long Swordsman",
        "Cost": {"Food": 60, "Gold": 20},
        "HP": 60,
        "Attack": 9,
        "Armor": 1,
        "Pierce Armor": 1,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "All-purpose infantry unit. Strong vs. buildings and infantry. Weak vs. archers at long range.",
        "Build Time": 21
    },

    "Two-Handed Swordsman": {
        "Name": "Two-Handed Swordsman",
        "Cost": {"Food": 60, "Gold": 20},
        "HP": 60,
        "Attack": 12,
        "Armor": 1,
        "Pierce Armor": 1,
        "Range": 0,
        "Line of Sight": 5,
        "Explanation Text": "All-purpose infantry unit. Strong vs. buildings and infantry. Weak vs. archers at long range.",
        "Build Time": 21
    },

    "Champion": {
        "Name": "Champion",
        "Cost": {"Food": 60, "Gold": 20},
        "HP": 70,
        "Attack": 13,
        "Armor": 1,
        "Pierce Armor": 1,
        "Range": 0,
        "Line of Sight": 5,
        "Explanation Text": "All-purpose infantry unit. Strong vs. buildings and infantry. Weak vs. archers at long range.",
        "Build Time": 21
    },

    "Spearman": {
        "Name": "Spearman",
        "Cost": {"Food": 35, "Wood": 25},
        "HP": 45,
        "Attack": 3,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Anti-cavalry infantry unit. Strong vs. mounted units, especially elephants. Weak vs. archers and infantry.",
        "Build Time": 22
    },

    "Pikeman": {
        "Name": "Pikeman",
        "Cost": {"Food": 35, "Wood": 25},
        "HP": 55,
        "Attack": 4,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Anti-cavalry infantry unit. Strong vs. mounted units, especially elephants. Weak vs. archers and infantry.",
        "Build Time": 22
    },

    "Halberdier": {
        "Name": "Halberdier",
        "Cost": {"Food": 35, "Wood": 25},
        "HP": 60,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Anti-cavalry infantry unit. Strong vs. mounted units, especially elephants. Weak vs. archers and infantry.",
        "Build Time": 22
    },

    # Archery Range
    "Archer": {
        "Name": "Archer",
        "Cost": {"Wood": 25, "Gold": 45},
        "HP": 30,
        "Attack": 4,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 4,
        "Line of Sight": 6,
        "Explanation Text": "Ranged unit. Strong vs. units at long range. Weak vs. Skirmishers and units at close range.",
        "Build Time": 35
    },

    "Crossbowman": {
        "Name": "Crossbowman",
        "Cost": {"Wood": 25, "Gold": 45},
        "HP": 35,
        "Attack": 5,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 5,
        "Line of Sight": 7,
        "Explanation Text": "Ranged unit. Strong vs. units at long range. Weak vs. Elite Skirmishers, Mangonels, and units at close range.",
        "Build Time": 27
    },

    "Arbalester": {
        "Name": "Arbalester",
        "Cost": {"Wood": 25, "Gold": 45},
        "HP": 40,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 5,
        "Line of Sight": 7,
        "Explanation Text": "Ranged unit. Strong vs. units at long range. Weak vs. Elite Skirmishers, Onagers, and units at close range.",
        "Build Time": 27
    },

    "Skirmisher": {
        "Name": "Skirmisher",
        "Cost": {"Food": 25, "Wood": 35},
        "HP": 30,
        "Attack": 2,
        "Armor": 0,
        "Pierce Armor": 3,
        "Range": 4,
        "Minimum Range": 1,
        "Line of Sight": 6,
        "Explanation Text": "Ranged anti-archer unit that cannot attack at close range. Strong vs. archers. Weak vs. units at close range.",
        "Build Time": 22
    },

    "Elite Skirmisher": {
        "Name": "Elite Skirmisher",
        "Cost": {"Food": 25, "Wood": 35},
        "HP": 35,
        "Attack": 3,
        "Armor": 0,
        "Pierce Armor": 4,
        "Range": 5,
        "Minimum Range": 1,
        "Line of Sight": 7,
        "Explanation Text": "Ranged anti-archer unit that cannot attack at close range. Strong vs. archers. Weak vs. units at close range.",
        "Build Time": 22
    },

    "Cavalry Archer": {
        "Name": "Cavalry Archer",
        "Cost": {"Wood": 40, "Gold": 60},
        "HP": 50,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 4,
        "Line of Sight": 5,
        "Explanation Text": "Mounted archer. Strong vs. slow units at long range. Weak vs. Elite Skirmishers and units at close range.",
        "Build Time": 34
    },

    "Heavy Cavalry Archer": {
        "Name": "Heavy Cavalry Archer",
        "Cost": {"Wood": 40, "Gold": 60},
        "HP": 60,
        "Attack": 7,
        "Armor": 1,
        "Pierce Armor": 0,
        "Range": 4,
        "Line of Sight": 6,
        "Explanation Text": "Mounted archer. Strong vs. slow units at long range. Weak vs. Elite Skirmishers and units at close range.",
        "Build Time": 27
    },

    "Hand Cannoneer": {
        "Name": "Hand Cannoneer",
        "Cost": {"Food": 45, "Gold": 50},
        "HP": 40,
        "Attack": 17,
        "Armor": 1,
        "Pierce Armor": 0,
        "Range": 7,
        "Line of Sight": 9,
        "Explanation Text": "Gunpowder unit with powerful attack, but inaccurate at long range. Strong vs. infantry. Weak vs. Elite Skirmishers and archers.",
        "Build Time": 34
    },

    # Stable
    "Scout Cavalry": {
        "Name": "Scout Cavalry",
        "Cost": {"Food": 80},
        "HP": 45,
        "Attack": 3,
        "Armor": 0,
        "Pierce Armor": 2,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Fast cavalry for scouting and raiding. Resistant to conversion. Strong vs. Monks. Weak vs. Pikemen and Camel Riders.",
        "Build Time": 30
    },

    "Light Cavalry": {
        "Name": "Light Cavalry",
        "Cost": {"Food": 80},
        "HP": 60,
        "Attack": 7,
        "Armor": 0,
        "Pierce Armor": 2,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Fast cavalry for scouting and raiding. Resistant to conversion. Strong vs. Monks. Weak vs. Pikemen and Camel Riders.",
        "Build Time": 30
    },

    "Hussar": {
        "Name": "Hussar",
        "Cost": {"Food": 80},
        "HP": 75,
        "Attack": 7,
        "Armor": 0,
        "Pierce Armor": 2,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Fast cavalry for scouting and raiding. Resistant to conversion. Strong vs. Monks. Weak vs. Pikemen and Camel Riders.",
        "Build Time": 30
    },

    "Camel Rider": {
        "Name": "Camel Rider",
        "Cost": {"Food": 55, "Gold": 60},
        "HP": 100,
        "Attack": 6,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Line of Sight": 5,
        "Explanation Text": "Fast anti-cavalry unit. Strong vs. cavalry. Weak vs. Spearmen, Monks, and archers.",
        "Build Time": 22
    },

    "Heavy Camel Rider": {
        "Name": "Heavy Camel Rider",
        "Cost": {"Food": 55, "Gold": 60},
        "HP": 120,
        "Attack": 7,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Line of Sight": 5,
        "Explanation Text": "Fast anti-cavalry unit. Strong vs. cavalry. Weak vs. Pikemen, Monks, and archers.",
        "Build Time": 22
    },

    "Knight": {
        "Name": "Knight",
        "Cost": {"Food": 60, "Gold": 75},
        "HP": 100,
        "Attack": 10,
        "Armor": 2,
        "Pierce Armor": 2,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Powerful all-purpose cavalry. Strong vs. infantry and archers. Weak vs. Pikemen, Camel Riders, and Monks.",
        "Build Time": 30
    },

    "Cavalier": {
        "Name": "Cavalier",
        "Cost": {"Food": 60, "Gold": 75},
        "HP": 120,
        "Attack": 12,
        "Armor": 2,
        "Pierce Armor": 2,
        "Range": 0,
        "Line of Sight": 4,
        "Explanation Text": "Powerful all-purpose cavalry. Strong vs. infantry and archers. Weak vs. Pikemen, Camel Riders, and Monks.",
        "Build Time": 30
    },

    "Paladin": {
        "Name": "Paladin",
        "Cost": {"Food": 60, "Gold": 75},
        "HP": 160,
        "Attack": 14,
        "Armor": 2,
        "Pierce Armor": 3,
        "Range": 0,
        "Line of Sight": 5,
        "Explanation Text": "Powerful all-purpose cavalry. Strong vs. infantry and archers. Weak vs. Halberdiers, Heavy Camel Riders, and Monks.",
        "Build Time": 30
    },

    # Siege Workshop
    "Battering Ram": {
        "Name": "Battering Ram",
        "Cost": {"Wood": 160, "Gold": 75},
        "HP": 175,
        "Attack": 2,
        "Armor": -3,
        "Pierce Armor": 180,
        "Range": 0,
        "Line of Sight": 3,
        "Explanation Text": "Anti-building siege weapon. Resistant to most ranged attacks. Garrisoned infantry increase speed and attack.",
        "Build Time": 36
    },

    "Capped Ram": {
        "Name": "Capped Ram",
        "Cost": {"Wood": 160, "Gold": 75},
        "HP": 200,
        "Attack": 3,
        "Armor": -3,
        "Pierce Armor": 190,
        "Range": 0,
        "Line of Sight": 3,
        "Explanation Text": "Anti-building siege weapon. Resistant to most ranged attacks. Garrisoned infantry increase speed and attack.",
        "Build Time": 36
    },

    "Siege Ram": {
        "Name": "Siege Ram",
        "Cost": {"Wood": 160, "Gold": 75},
        "HP": 270,
        "Attack": 4,
        "Armor": -3,
        "Pierce Armor": 195,
        "Range": 0,
        "Line of Sight": 3,
        "Explanation Text": "Anti-building siege weapon. Resistant to most ranged attacks. Garrisoned infantry increase speed and attack.",
        "Build Time": 36
    },

    "Mangonel": {
        "Name": "Mangonel",
        "Cost": {"Wood": 160, "Gold": 135},
        "HP": 50,
        "Attack": 40,
        "Armor": 0,
        "Pierce Armor": 6,
        "Range": 7,
        "Minimum Range": 3,
        "Line of Sight": 9,
        "Explanation Text": "Ranged siege weapon with area of effect attack, but cannot attack enemies at close range. Strong vs. tight groups of units. Can attack ground.",
        "Build Time": 46
    },

    "Onager": {
        "Name": "Onager",
        "Cost": {"Wood": 160, "Gold": 75},
        "HP": 60,
        "Attack": 50,
        "Armor": 0,
        "Pierce Armor": 7,
        "Range": 8,
        "Minimum Range": 3,
        "Line of Sight": 10,
        "Explanation Text": "Ranged siege weapon with area of effect attack, but cannot attack enemies at close range. Strong vs. tight groups of units. Can attack ground and destroy trees.",
        "Build Time": 46
    },

    "Siege Onager": {
        "Name": "Siege Onager",
        "Cost": {"Wood": 160, "Gold": 75},
        "HP": 70,
        "Attack": 75,
        "Armor": 0,
        "Pierce Armor": 8,
        "Range": 8,
        "Minimum Range": 3,
        "Line of Sight": 10,
        "Explanation Text": "Ranged siege weapon with area of effect attack, but cannot attack enemies at close range. Strong vs. tight groups of units. Can attack ground and destroy trees.",
        "Build Time": 46
    },

    "Scorpion": {
        "Name": "Scorpion",
        "Cost": {"Wood": 75, "Gold": 75},
        "HP": 40,
        "Attack": 12,
        "Armor": 0,
        "Pierce Armor": 7,
        "Range": 7,
        "Minimum Range": 2,
        "Line of Sight": 9,
        "Explanation Text": "Anti-unit siege weapon. Fires bolts that pierce multiple units. Strong vs. large groups of units. Weak vs. cavalry and siege weapons.",
        "Build Time": 30
    },

    "Heavy Scorpion": {
        "Name": "Heavy Scorpion",
        "Cost": {"Wood": 75, "Gold": 75},
        "HP": 50,
        "Attack": 16,
        "Armor": 0,
        "Pierce Armor": 8,
        "Range": 7,
        "Minimum Range": 2,
        "Line of Sight": 9,
        "Explanation Text": "Anti-unit siege weapon. Fires bolts that pierce multiple units. Strong vs. large groups of units. Weak vs. cavalry and siege weapons.",
        "Build Time": 30
    },

    "Bombard Cannon": {
        "Name": "Bombard Cannon",
        "Cost": {"Wood": 225, "Gold": 225},
        "HP": 80,
        "Attack": 40,
        "Armor": 2,
        "Pierce Armor": 5,
        "Range": 12,
        "Minimum Range": 5,
        "Line of Sight": 14,
        "Explanation Text": "Anti-unit siege weapon. Fires bolts that pierce multiple units. Strong vs. large groups of units. Weak vs. cavalry and siege weapons.",
        "Build Time": 30
    },

    "Siege Tower": {
        "Name": "Siege Tower",
        "Cost": {"Wood": 200, "Gold": 160},
        "HP": 220,
        "Attack": 16,
        "Armor": -2,
        "Pierce Armor": 100,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 8,
        "Garrison": 10,
        "Explanation Text": "Quick land transport used to unload units over enemy walls. Resistant to archer attack. Cannot be used by mounted units.",
        "Build Time": 36
    },

    # Castle
    "Petard": {
        "Name": "Petard",
        "Cost": {"Food": 65, "Gold": 20},
        "HP": 50,
        "Attack": 25,
        "Armor": 0,
        "Pierce Armor": 2,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 4,
        "Garrison": 0,
        "Explanation Text": "Demolition siege unit armed with explosives. Strong vs. buildings. Weak vs. other units. Self-destructs when used.",
        "Build Time": 25
    },

    "Trebuchet": {
        "Name": "Trebuchet",
        "Cost": {"Wood": 200, "Gold": 200},
        "HP": 150,
        "Attack": 200,
        "Armor": 2,
        "Pierce Armor": 8,
        "Range": 16,
        "Minimum Range": 4,
        "Line of Sight": 19,
        "Garrison": 0,
        "Explanation Text": "Powerful anti-building siege weapon with long range. Must be packed to move, unpacked to attack. Cannot attack enemies at close range. Strong vs. buildings. Can attack ground and destroy trees.",
        "Build Time": 50
    },

    # Monastery
    "Monk": {
        "Name": "Monk",
        "Cost": {"Gold": 100},
        "HP": 30,
        "Attack": 0,
        "Armor": 0,
        "Pierce Armor": 0,
        "Range": 0,
        "Minimum Range": 0,
        "Line of Sight": 11,
        "Garrison": 0,
        "Explanation Text": "Converts enemy units to your civilization. Heals friendly units (except ships and siege weapons). Strong vs. slow and non-ranged units. Weak vs. Light Cavalry and ranged units. Can collect Relics and bring them to Monasteries.",
        "Build Time": 51
    },

}


unique_units = {

    "Teutons": {
        "Teutonic Knight": {
            "Name": "Teutonic Knight",
            "Cost": {"Food": 85, "Gold": 40},
            "Explanation Text": "Teutonic unique infantry unit. Slow and powerful. Strong vs. melee units. Weak vs. archers and Scorpions.",
            "Research Time": 12,
        },

        "Elite Teutonic Knight": {
            "Name": "Elite Teutonic Knight",
            "Cost": {"Food": 85, "Gold": 40},
            "Explanation Text": "Teutonic unique infantry unit. Slow and powerful. Strong vs. melee units. Weak vs. archers and Scorpions.",
            "Research Time": 12,
        },
    }
}