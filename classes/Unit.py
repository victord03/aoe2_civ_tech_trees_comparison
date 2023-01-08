
class Unit:
    """Unit class.

    Handles all Unit data.
    """
    name: str
    cost: dict
    hp: int
    attack: int
    range: float
    line_of_sight: int
    armor: int
    pierce_armor: int
    build_time: int
    # todo: think about a 'requirements: list' attribute

    #### Barracks

    # Militia-line
    def create_militia(self):
        """Generates data for the Militia unit."""
        self.name = "Militia"
        self.cost = {"Food": 60, "Gold": 20}
        self.hp = 40
        self.attack = 4
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 1
        self.build_time = 21

    def create_man_at_arms(self):
        """Generates data for the Man-at-Arms unit."""
        self.name = "Man-at-Arms"
        self.cost = {"Food": 60, "Gold": 20}
        self.hp = 45
        self.attack = 6
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 1
        self.build_time = 21

    def create_long_swordsman(self):
        """Generates data for the Long Swordsman unit."""
        self.name = "Long Swordsman"
        self.cost = {"Food": 60, "Gold": 20}
        self.hp = 60
        self.attack = 9
        self.range = 0
        self.line_of_sight = 4
        self.armor = 1
        self.pierce_armor = 1
        self.build_time = 21

    def create_two_handed_swordsman(self):
        """Generates data for the Two-Handed Swordsman unit."""
        self.name = "Two-Handed Swordsman"
        self.cost = {"Food": 60, "Gold": 20}
        self.hp = 60
        self.attack = 12
        self.range = 0
        self.line_of_sight = 5
        self.armor = 1
        self.pierce_armor = 1
        self.build_time = 21

    def create_champion(self):
        """Generates data for the Champion unit."""
        self.name = "Champion"
        self.cost = {"Food": 60, "Gold": 20}
        self.hp = 70
        self.attack = 13
        self.range = 0
        self.line_of_sight = 5
        self.armor = 1
        self.pierce_armor = 1
        self.build_time = 21

    # Spearman-line
    def create_spearman(self):
        """Generates data for the Spearman unit."""
        self.name = "Spearman"
        self.cost = {"Food": 35, "Wood": 25}
        self.hp = 45
        self.attack = 3
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 22

    def create_pikeman(self):
        """Generates data for the Pikeman unit."""
        self.name = "Pikeman"
        self.cost = {"Food": 35, "Wood": 25}
        self.hp = 55
        self.attack = 4
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 22

    def create_halberdier(self):
        """Generates data for the Halberdier unit."""
        self.name = "Halberdier"
        self.cost = {"Food": 35, "Wood": 25}
        self.hp = 60
        self.attack = 6
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 22

    # Eagle-line
    def create_eagle_scout(self):
        """Generates data for the Eagle Scout unit."""
        self.name = "Eagle Scout"
        self.cost = {"Food": 20, "Gold": 50}
        self.hp = 50
        self.attack = 4
        self.range = 0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 60

    def create_eagle_warrior(self):
        """Generates data for the Eagle Warrior unit."""
        self.name = "Eagle Warrior"
        self.cost = {"Food": 20, "Gold": 50}
        self.hp = 55
        self.attack = 7
        self.range = 0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 3
        self.build_time = 35

    def create_elite_eagle_warrior(self):
        """Generates data for the Elite Eagle Warrior unit."""
        self.name = "Elite Eagle Warrior"
        self.cost = {"Food": 20, "Gold": 50}
        self.hp = 60
        self.attack = 9
        self.range = 0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 20

    #### Archery Range

    # Archer-line
    def create_archer(self):
        """Generates data for the Archer unit."""
        self.name = "Archer"
        self.cost = {"Wood": 25, "Gold": 45}
        self.hp = 30
        self.attack = 4
        self.range = 4
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 35

    def create_crossbowman(self):
        """Generates data for the Crossbowman unit."""
        self.name = "Crossbowman"
        self.cost = {"Wood": 25, "Gold": 45}
        self.hp = 35
        self.attack = 5
        self.range = 5
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 27

    def create_arbalester(self):
        """Generates data for the Arbalester unit."""
        self.name = "Arbalester"
        self.cost = {"Wood": 25, "Gold": 45}
        self.hp = 40
        self.attack = 6
        self.range = 5
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 27

    # Skirmisher-line
    def create_Skirmisher(self):
        """Generates data for the Skirmisher unit."""
        self.name = "Skirmisher"
        self.cost = {"Food": 25, "Wood": 35}
        self.hp = 30
        self.attack = 2
        self.range = 4
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 3
        self.build_time = 22

    def create_elite_skirmisher(self):
        """Generates data for the Elite Skirmisher unit."""
        self.name = "Elite Skirmisher"
        self.cost = {"Food": 25, "Wood": 35}
        self.hp = 35
        self.attack = 3
        self.range = 5
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 22

    # Cavalry Archer-line
    def create_cavalry_archer(self):
        """Generates data for the Cavalry Archer unit."""
        self.name = "Cavalry Archer"
        self.cost = {"Wood": 40, "Gold": 60}
        self.hp = 50
        self.attack = 6
        self.range = 4
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 34

    def create_heavy_cavalry_archer(self):
        """Generates data for the Heavy Cavalry Archer unit."""
        self.name = "Heavy Cavalry Archer"
        self.cost = {"Wood": 40, "Gold": 60}
        self.hp = 60
        self.attack = 7
        self.range = 4
        self.line_of_sight = 6
        self.armor = 1
        self.pierce_armor = 0
        self.build_time = 27

    # Hand Cannoneer
    def create_hand_cannoneer(self):
        """Generates data for the Hand Cannoneer unit."""
        self.name = "Hand Cannoneer"
        self.cost = {"Food": 45, "Gold": 50}
        self.hp = 40
        self.attack = 17
        self.range = 7
        self.line_of_sight = 9
        self.armor = 1
        self.pierce_armor = 0
        self.build_time = 34

    #### Stable

    # Scout Cavalry-line
    def create_scout_cavalry(self):
        """Generates data for the Scout Cavalry unit."""
        self.name = "Scout Cavalry"
        self.cost = {"Food": 80}
        self.hp = 45
        self.attack = 3
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 30

    def create_light_cavalry(self):
        """Generates data for the Light Cavalry unit."""
        self.name = "Light Cavalry"
        self.cost = {"Food": 80}
        self.hp = 60
        self.attack = 7
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 30

    def create_hussar(self):
        """Generates data for the Hussar unit."""
        self.name = "Hussar"
        self.cost = {"Food": 80}
        self.hp = 75
        self.attack = 7
        self.range = 0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 30

    # Camel Rider-line
    def create_camel_rider(self):
        """Generates data for the Camel Rider unit."""
        self.name = "Camel Rider"
        self.cost = {"Food": 55, "Gold": 60}
        self.hp = 100
        self.attack = 6
        self.range = 0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 22

    def create_heavy_camel_rider(self):
        """Generates data for the Heavy Camel Rider unit."""
        self.name = "Heavy Camel Rider"
        self.cost = {"Food": 45, "Gold": 50}
        self.hp = 120
        self.attack = 7
        self.range = 0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 22

    # Knight-line
    def create_knight(self):
        """Generates data for the Knight unit."""
        self.name = "Knight"
        self.cost = {"Food": 60, "Gold": 75}
        self.hp = 100
        self.attack = 10
        self.range = 0
        self.line_of_sight = 4
        self.armor = 2
        self.pierce_armor = 2
        self.build_time = 30

    def create_cavalier(self):
        """Generates data for the Cavalier unit."""
        self.name = "Cavalier"
        self.cost = {"Food": 60, "Gold": 75}
        self.hp = 120
        self.attack = 12
        self.range = 0
        self.line_of_sight = 4
        self.armor = 2
        self.pierce_armor = 2
        self.build_time = 30

    def create_paladin(self):
        """Generates data for the Paladin unit."""
        self.name = "Paladin"
        self.cost = {"Food": 60, "Gold": 75}
        self.hp = 160
        self.attack = 14
        self.range = 0
        self.line_of_sight = 5
        self.armor = 2
        self.pierce_armor = 3
        self.build_time = 30

    #### Dock

    # Fishing Ship
    def create_fishing_ship(self):
        """Generates data for the Fishing Ship unit."""
        self.name = "Fishing Ship"
        self.cost = {"Wood": 75}
        self.hp = 60
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 40

    # Transport Ship
    def create_transport_ship(self):
        """Generates data for the Transport Ship unit."""
        self.name = "Transport Ship"
        self.cost = {"Wood": 125}
        self.hp = 100
        self.line_of_sight = 5
        self.armor = 4
        self.pierce_armor = 8
        self.build_time = 46

    # Trade Cog
    def create_trade_cog(self):
        """Generates data for the Trade Cog unit."""
        self.name = "Trade Cog"
        self.cost = {"Wood": 100, "Gold": 50}
        self.hp = 80
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 36

    # Fish Trap
    def create_fish_trap(self):
        """Generates data for the Fish Trap unit."""
        self.name = "Fish Trap"
        self.cost = {"Wood": 100}
        self.hp = 50
        self.line_of_sight = 1
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 40

    # Fire Galley-line
    def create_fire_galley(self):
        """Generates data for the Fire Galley unit."""
        self.name = "Fire Galley"
        self.cost = {"Wood": 75, "Gold": 45}
        self.hp = 100
        self.attack = 1
        self.range = 0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 25

    def create_fire_ship(self):
        """Generates data for the Fire Ship unit."""
        self.name = "Fire Ship"
        self.cost = {"Wood": 75, "Gold": 45}
        self.hp = 100
        self.attack = 1
        self.range = 2.5
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 25

    def create_fast_fire_ship(self):
        """Generates data for the Fast Fire Ship unit."""
        self.name = "Fast Fire Ship"
        self.cost = {"Wood": 75, "Gold": 45}
        self.hp = 120
        self.attack = 2
        self.range = 2.5
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 4
        self.build_time = 25

    # Demolition Raft-line
    def create_demolition_raft(self):
        """Generates data for the Demolition Raft unit."""
        self.name = "Demolition Raft"
        self.cost = {"Wood": 70, "Gold": 50}
        self.hp = 45
        self.attack = 90
        self.range = 0.0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 45

    def create_demolition_ship(self):
        """Generates data for the Demolition Ship unit."""
        self.name = "Demolition Ship"
        self.cost = {"Wood": 70, "Gold": 50}
        self.hp = 60
        self.attack = 110
        self.range = 0.0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 31

    def create_heavy_demolition_ship(self):
        """Generates data for the Heavy Demolition Ship unit."""
        self.name = "Heavy Demolition Ship"
        self.cost = {"Wood": 70, "Gold": 50}
        self.hp = 70
        self.attack = 140
        self.range = 0.0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 5
        self.build_time = 31

    # Galley-line
    def create_galley(self):
        """Generates data for the Galley unit."""
        self.name = "Galley"
        self.cost = {"Wood": 90, "Gold": 30}
        self.hp = 120
        self.attack = 5
        self.range = 5.0
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 60

    def create_war_galley(self):
        """Generates data for the War Galley unit."""
        self.name = "War Galley"
        self.cost = {"Wood": 90, "Gold": 30}
        self.hp = 135
        self.attack = 7
        self.range = 6.0
        self.line_of_sight = 8
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 36

    def create_galleon(self):
        """Generates data for the Galleon unit."""
        self.name = "Galleon"
        self.cost = {"Wood": 90, "Gold": 30}
        self.hp = 165
        self.attack = 8
        self.range = 7.0
        self.line_of_sight = 9
        self.armor = 0
        self.pierce_armor = 8
        self.build_time = 36

    # Cannon Galleon-line
    def create_cannon_galleon(self):
        """Generates data for the Cannon Galleon unit."""
        self.name = "Cannon Galleon"
        self.cost = {"Wood": 200, "Gold": 150}
        self.hp = 120
        self.attack = 35
        self.range = 13.0
        self.line_of_sight = 15
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 46

    def create_elite_cannon_galleon(self):
        """Generates data for the Elite Cannon Galleon unit."""
        self.name = "Elite Cannon Galleon"
        self.cost = {"Wood": 200, "Gold": 150}
        self.hp = 150
        self.attack = 45
        self.range = 15.0
        self.line_of_sight = 17
        self.armor = 0
        self.pierce_armor = 8
        self.build_time = 46

    #### Town Center

    def create_villager(self):
        """Generates data for the Villager unit."""
        self.name = "Villager"
        self.cost = {"Food": 50}
        self.hp = 25
        self.attack = 3
        self.range = 0.0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 25

    #### Mill

    def create_farm(self):
        """Generates data for the Farm unit."""
        self.name = "Farm"
        self.cost = {"Wood": 60}
        self.hp = 480
        self.line_of_sight = 1
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 15


    #### Siege Workshop

    # Battering Ram-line
    def create_battering_ram(self):
        """Generates data for the Battering Ram unit."""
        self.name = "Battering Ram"
        self.cost = {"Wood": 160, "Gold": 75}
        self.hp = 175
        self.attack = 2
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = -3
        self.pierce_armor = 180
        self.build_time = 36

    def create_capped_ram(self):
        """Generates data for the Capped Ram unit."""
        self.name = "Capped Ram"
        self.cost = {"Wood": 160, "Gold": 75}
        self.hp = 200
        self.attack = 3
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = -3
        self.pierce_armor = 190
        self.build_time = 36

    def create_siege_ram(self):
        """Generates data for the Siege Ram unit."""
        self.name = "Siege Ram"
        self.cost = {"Wood": 160, "Gold": 75}
        self.hp = 270
        self.attack = 4
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = -3
        self.pierce_armor = 195
        self.build_time = 36

    # Mangonel-line
    def create_mangonel(self):
        """Generates data for the Mangonel unit."""
        self.name = "Mangonel"
        self.cost = {"Wood": 160, "Gold": 135}
        self.hp = 50
        self.attack = 40
        self.range = 7.0
        self.line_of_sight = 9
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 46

    def create_onager(self):
        """Generates data for the Onager unit."""
        self.name = "Onager"
        self.cost = {"Wood": 160, "Gold": 135}
        self.hp = 60
        self.attack = 50
        self.range = 8.0
        self.line_of_sight = 10
        self.armor = 0
        self.pierce_armor = 7
        self.build_time = 46

    def create_siege_onager(self):
        """Generates data for the Siege Onager unit."""
        self.name = "Siege Onager"
        self.cost = {"Wood": 160, "Gold": 135}
        self.hp = 70
        self.attack = 75
        self.range = 8.0
        self.line_of_sight = 10
        self.armor = 0
        self.pierce_armor = 8
        self.build_time = 46

    # Scorpion-line
    def create_scorpion(self):
        """Generates data for the Scorpion unit."""
        self.name = "Scorpion"
        self.cost = {"Wood": 75, "Gold": 75}
        self.hp = 40
        self.attack = 12
        self.range = 7.0
        self.line_of_sight = 9
        self.armor = 0
        self.pierce_armor = 7
        self.build_time = 30

    def create_heavy_scorpion(self):
        """Generates data for the Heavy Scorpion unit."""
        self.name = "Heavy Scorpion"
        self.cost = {"Wood": 75, "Gold": 75}
        self.hp = 50
        self.attack = 16
        self.range = 7.0
        self.line_of_sight = 9
        self.armor = 0
        self.pierce_armor = 8
        self.build_time = 30

    # Bombard Cannon
    def create_bombard_cannon(self):
        """Generates data for the Bombard Cannon unit."""
        self.name = "Bombard Cannon"
        self.cost = {"Wood": 225, "Gold": 225}
        self.hp = 80
        self.attack = 40
        self.range = 12.0
        self.line_of_sight = 14
        self.armor = 2
        self.pierce_armor = 5
        self.build_time = 56

    # Siege Tower
    def create_siege_tower(self):
        """Generates data for the Siege Tower unit."""
        self.name = "Siege Tower"
        self.cost = {"Wood": 200, "Gold": 160}
        self.hp = 220
        self.line_of_sight = 8
        self.armor = -2
        self.pierce_armor = 100
        self.build_time = 36

    #### Castle

    # Unique Units
    # Teutonic Knight (Teutons)
    def create_teutonic_knight(self):
        """Generates data for the Teutonic Knight unit."""
        self.name = "Teutonic Knight"
        self.cost = {"Food": 85, "Gold": 40}
        self.hp = 80
        self.attack = 14
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = 7
        self.pierce_armor = 2
        self.build_time = 12

    def create_elite_teutonic_knight(self):
        """Generates data for the Elite Teutonic Knight unit."""
        self.name = "Elite Teutonic Knight"
        self.cost = {"Food": 85, "Gold": 40}
        self.hp = 100
        self.attack = 17
        self.range = 0.0
        self.line_of_sight = 5
        self.armor = 10
        self.pierce_armor = 2
        self.build_time = 12

    # Huskarl (Goths)
    def create_huskarl(self):
        """Generates data for the Huskarl unit."""
        self.name = "Huskarl"
        self.cost = {"Food": 80, "Gold": 40}
        self.hp = 60
        self.attack = 10
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = 0
        self.pierce_armor = 6
        self.build_time = 16

    def create_elite_huskarl(self):
        """Generates data for the Elite Huskarl unit."""
        self.name = "Elite Huskarl"
        self.cost = {"Food": 80, "Gold": 40}
        self.hp = 70
        self.attack = 12
        self.range = 0.0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 8
        self.build_time = 16

    # Woad Raider
    def create_woad_raider(self):
        """Generates data for the Woad Raider unit."""
        self.name = "Woad Raider"
        self.cost = {"Food": 65, "Gold": 25}
        self.hp = 65
        self.attack = 10
        self.range = 0.0
        self.line_of_sight = 3
        self.armor = 0
        self.pierce_armor = 1
        self.build_time = 10

    def create_elite_woad_raider(self):
        """Generates data for the Elite Woad Raider unit."""
        self.name = "Elite Woad Raider"
        self.cost = {"Food": 65, "Gold": 25}
        self.hp = 80
        self.attack = 13
        self.range = 0.0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 1
        self.build_time = 10

    # Cataphract
    def create_cataphract(self):
        """Generates data for the Cataphract unit."""
        self.name = "Cataphract"
        self.cost = {"Food": 70, "Gold": 75}
        self.hp = 110
        self.attack = 9
        self.range = 0.0
        self.line_of_sight = 4
        self.armor = 2
        self.pierce_armor = 1
        self.build_time = 20

    def create_elite_cataphract(self):
        """Generates data for the Elite Cataphract unit."""
        self.name = "Elite Cataphract"
        self.cost = {"Food": 70, "Gold": 75}
        self.hp = 150
        self.attack = 12
        self.range = 0.0
        self.line_of_sight = 5
        self.armor = 2
        self.pierce_armor = 1
        self.build_time = 20

    # Mangudai (Mongols)
    def create_mangudai(self):
        """Generates data for the Cataphract unit."""
        self.name = "Mangudai"
        self.cost = {"Wood": 55, "Gold": 65}
        self.hp = 60
        self.attack = 6
        self.range = 4.0
        self.line_of_sight = 6
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 26

    def create_elite_mangudai(self):
        """Generates data for the Cataphract unit."""
        self.name = "Elite Mangudai"
        self.cost = {"Wood": 55, "Gold": 65}
        self.hp = 60
        self.attack = 8
        self.range = 4.0
        self.line_of_sight = 6
        self.armor = 1
        self.pierce_armor = 0
        self.build_time = 26

    # Longbowman
    def create_longbowman(self):
        """Generates data for the Longbowman unit."""
        self.name = "Longbowman"
        self.cost = {"Wood": 35, "Gold": 40}
        self.hp = 35
        self.attack = 6
        self.range = 5.0
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 18

    def create_elite_longbowman(self):
        """Generates data for the Elite Longbowman unit."""
        self.name = "Elite Longbowman"
        self.cost = {"Wood": 35, "Gold": 40}
        self.hp = 40
        self.attack = 7
        self.range = 6.0
        self.line_of_sight = 8
        self.armor = 0
        self.pierce_armor = 1
        self.build_time = 18

    # Throwing Axeman
    def create_throwing_axeman(self):
        """Generates data for the Throwing Axeman unit."""
        self.name = "Throwing Axeman"
        self.cost = {"Food": 55, "Gold": 25}
        self.hp = 60
        self.attack = 7
        self.range = 3.0
        self.line_of_sight = 5
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 17

    def create_elite_throwing_axeman(self):
        """Generates data for the Elite Throwing Axeman unit."""
        self.name = "Elite Throwing Axeman"
        self.cost = {"Food": 55, "Gold": 25}
        self.hp = 70
        self.attack = 8
        self.range = 4.0
        self.line_of_sight = 6
        self.armor = 1
        self.pierce_armor = 0
        self.build_time = 17

    # Petard
    def create_petard(self):
        """Generates data for the Petard unit."""
        self.name = "Petard"
        self.cost = {"Food": 65, "Gold": 20}
        self.hp = 50
        self.attack = 25
        self.range = 0.0
        self.line_of_sight = 4
        self.armor = 0
        self.pierce_armor = 2
        self.build_time = 25

    # Trebuchet
    def create_trebuchet(self):
        """Generates data for the Trebuchet unit."""
        self.name = "Trebuchet"
        self.cost = {"Wood": 200, "Gold": 200}
        self.hp = 150
        self.attack = 200
        self.range = 16.0
        self.line_of_sight = 19
        self.armor = 2
        self.pierce_armor = 8
        self.build_time = 50

    #### Monastery

    # Monk
    def create_monk(self):
        """Generates data for the Monk unit."""
        self.name = "Monk"
        self.cost = {"Gold": 100}
        self.hp = 30
        self.line_of_sight = 11
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 51

    #### Market

    # Trade Cart
    def create_trade_cart(self):
        """Generates data for the Trade Cart unit."""
        self.name = "Trade Cart"
        self.cost = {"Wood": 100, "Gold": 50}
        self.hp = 70
        self.line_of_sight = 7
        self.armor = 0
        self.pierce_armor = 0
        self.build_time = 51
