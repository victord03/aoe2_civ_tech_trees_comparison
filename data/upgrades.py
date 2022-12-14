

upgrades = {

    # Barracks
    "Man-at-Arms": {
        "Name": "Man-at-Arms Upgrade",
        "Cost": {"Food": 100, "Gold": 40},
        "Explanation Text": "Allows building Man-at-Arms.",
        "Research Time": 40
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

}


#### Blacksmith

# Archer armor upgrades
def research_padded_archer_armor(self):
    self.name = "Padded Archer Armor"
    self.cost = {"Food": 100}
    self.explanation_text = "Archers and cavalry archers have +1 normal/+1 pierce armor."
    self.research_time = 40


def research_leather_archer_armor(self):
    self.name = "Leather Archer Armor"
    self.cost = {"Food": 100, "Gold": 150}
    self.explanation_text = "Archers and cavalry archers have +1 normal/+1 pierce armor."
    self.research_time = 55


def research_ring_archer_armor(self):
    self.name = "Ring Archer Armor"
    self.cost = {"Food": 250, "Gold": 250}
    self.explanation_text = "Archers and cavalry archers have +1 normal/+2 pierce armor."
    self.research_time = 70


# Archers, towers and town centers attack & range upgrades
def research_fletching(self):
    self.name = "Fletching"
    self.cost = {"Food": 100, "Gold": 50}
    self.explanation_text = "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack."
    self.research_time = 30


def research_bodkin_arrow(self):
    self.name = "Bodkin Arrow"
    self.cost = {"Food": 200, "Gold": 100}
    self.explanation_text = "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack."
    self.research_time = 35


def research_bracer(self):
    self.name = "Bracer"
    self.cost = {"Food": 300, "Gold": 200}
    self.explanation_text = "Archers, cavalry archers, galleys, Castles, and towers have +1 attack and +1 range. Town Centers have +1 attack."
    self.research_time = 40

# Infantry and Cavalry attack upgrades
def research_forging(self):
    self.name = "Forging"
    self.cost = {"Food": 100}
    self.explanation_text = "Infantry and cavalry have +1 attack."
    self.research_time = 50

def research_iron_casting(self):
    self.name = "Iron Casting"
    self.cost = {"Food": 220, "Wood": 120}
    self.explanation_text = "Infantry and cavalry have +1 attack."
    self.research_time = 75

def research_blast_furnace(self):
    self.name = "Blast Furnace"
    self.cost = {"Food": 275, "Wood": 225}
    self.explanation_text = "Infantry and cavalry have +2 attack."
    self.research_time = 100

# Cavalry armor upgrades
def research_scale_barding_armor(self):
    self.name = "Scale Barding Armor"
    self.cost = {"Food": 150}
    self.explanation_text = "Cavalry have +1 normal/+1 pierce armor."
    self.research_time = 45

def research_chain_barding_armor(self):
    self.name = "Chain Barding Armor"
    self.cost = {"Food": 250, "Gold": 150}
    self.explanation_text = "Cavalry have +1 normal/+1 pierce armor."
    self.research_time = 60

def research_plate_barding_armor(self):
    self.name = "Plate Barding Armor"
    self.cost = {"Food": 350, "Gold": 200}
    self.explanation_text = "Cavalry have +1 normal/+2 pierce armor."
    self.research_time = 75

# Infantry armor upgrades
def research_scale_mail_armor(self):
    self.name = "Scale Mail Armor"
    self.cost = {"Food": 100}
    self.explanation_text = "Infantry have +1 normal/+1 pierce armor."
    self.research_time = 40

def research_chain_mail_armor(self):
    self.name = "Chain Mail Armor"
    self.cost = {"Food": 200, "Gold": 100}
    self.explanation_text = "Infantry have +1 normal/+1 pierce armor."
    self.research_time = 55

def research_plate_mail_armor(self):
    self.name = "Plate Mail Armor"
    self.cost = {"Food": 300, "Gold": 150}
    self.explanation_text = "Infantry have +1 normal/+2 pierce armor."
    self.research_time = 70



#### Archery Range
def research_thumb_ring(self):
    self.name = "Thumb Ring"
    self.cost = {"Food": 300, "Wood": 250}
    self.explanation_text = "Archers fire faster and with 100% accuracy."
    self.research_time = 45

def research_parthian_tactics(self):
    self.name = "Parthian Tactics"
    self.cost = {"Food": 200, "Gold": 250}
    self.explanation_text = "Mounted Archers have +1 normal/+2 pierce armor; Cavalry Archers have +4, Unique Mounted Archers +2 attack vs. pikemen."
    self.research_time = 65

#### Stable
def research_bloodlines(self):
    self.name = "Bloodlines"
    self.cost = {"Food": 150, "Gold": 100}
    self.explanation_text = "Mounted units have +20 hit points."
    self.research_time = 50

def research_husbandry(self):
    self.name = "Husbandry"
    self.cost = {"Food": 150}
    self.explanation_text = "Cavalry move 10% faster."
    self.research_time = 40


#### Siege Workshop


### Castle
def research_hoardings(self):
    self.name = "Hoardings"
    self.cost = {"Food": 400, "Wood": 400}
    self.explanation_text = "Strengthens Castles by providing +20% hit points."
    self.research_time = 75

def research_sappers(self):
    self.name = "Sappers"
    self.cost = {"Food": 400, "Gold": 200}
    self.explanation_text = "Villagers cause +15 damage when attacking buildings."
    self.research_time = 10

def research_conscription(self):
    self.name = "Conscription"
    self.cost = {"Food": 150, "Gold": 150}
    self.explanation_text = "Military buildings (except Siege Workshops) work 33% faster."
    self.research_time = 60

# Unique Techs
# Ironclad (Teutons, Castle Age)
def research_ironclad(self):
    self.name = "Ironclad"
    self.cost = {"Wood": 400, "Gold": 350}
    self.explanation_text = "Increases the armor of all siege weapons so they're more resistant to melee attack."
    self.research_time = 60

# Crenellations (Teutons, Imperial Age)
def research_crenellations(self):
    self.name = "Crenellations"
    self.cost = {"Food": 600, "Stone": 400}
    self.explanation_text = "Castles have +3 range; garrisoned infantry fire arrows."
    self.research_time = 60

# Nomads (Mongols, Castle Age)
def research_nomads(self):
    self.name = "Nomads"
    self.cost = {"Wood": 300, "Gold": 150}
    self.explanation_text = "Houses don't lose their population room when they are destroyed."
    self.research_time = 40

# Drill (Mongols, Imperial Age)
def research_drill(self):
    self.name = "Drill"
    self.cost = {"Wood": 500, "Gold": 450}
    self.explanation_text = "Siege Workshop units move 50% faster."
    self.research_time = 60

# Anarchy (Goths, Castle Age)
def research_anarchy(self):
    self.name = "Anarchy"
    self.cost = {"Food": 450, "Gold": 250}
    self.explanation_text = "Allows Huskarls to be created at the Barracks."
    self.research_time = 40

# Perfusion (Goths, Imperial Age)
def research_perfusion(self):
    self.name = "Perfusion"
    self.cost = {"Wood": 400, "Gold": 600}
    self.explanation_text = "Barracks units are created 100% faster."
    self.research_time = 40

# Bearded Axe (Franks, Castle Age)
def research_bearded_axe(self):
    self.name = "Bearded Axe"
    self.cost = {"Food": 300, "Gold": 300}
    self.explanation_text = "Throwing Axemen have +1 range."
    self.research_time = 60

# Chivalry (Franks, Imperial Age)
def research_chivalry(self):
    self.name = "Chivalry"
    self.cost = {"Wood": 600, "Gold": 500}
    self.explanation_text = "Increases the production speed of stables by +40%."
    self.research_time = 60

# Yeomen (Britons, Castle Age)
def research_yeomen(self):
    self.name = "Yeomen"
    self.cost = {"Wood": 750, "Gold": 450}
    self.explanation_text = "Foot archers have +1 range; towers have +2 attack."
    self.research_time = 60

# Warwolf (Britons, Imperial Age)
def research_warwolf(self):
    self.name = "Warwolf"
    self.cost = {"Wood": 800, "Gold": 400}
    self.explanation_text = "Improves your Trebuchets by giving them blast damage."
    self.research_time = 40

# Greek Fire (Byzantines, Castle Age)
def research_greek_fire(self):
    self.name = "Greek Fire"
    self.cost = {"Food": 250, "Gold": 300}
    self.explanation_text = "Fire Ships have +1 range."
    self.research_time = 40

# Logistica (Byzantines, Imperial Age)
def research_logistica(self):
    self.name = "Logistica"
    self.cost = {"Food": 800, "Gold": 600}
    self.explanation_text = "Cataphracts cause trample damage."
    self.research_time = 50

# Stronghold (Celts, Castle Age)
def research_stronghold(self):
    self.name = "Stronghold"
    self.cost = {"Food": 250, "Gold": 200}
    self.explanation_text = "Makes your castles and towers stronger by making them fire 25% faster."
    self.research_time = 30

# Furor Celtica (Celts, Imperial Age)
def research_furor_celtica(self):
    self.name = "Furor Celtica"
    self.cost = {"Food": 750, "Gold": 450}
    self.explanation_text = "Siege Workshop units have +40% hit points."
    self.research_time = 50

#### Town Center
def research_loom(self):
    self.name = "Loom"
    self.cost = {"Gold": 50}
    self.explanation_text = "Makes your villagers harder to kill by providing +15 hit points and +1 normal/+2 pierce armor."
    self.research_time = 25

def research_wheelbarrow(self):
    self.name = "Wheelbarrow"
    self.cost = {"Food": 175, "Wood": 50}
    self.explanation_text = "Villagers work more efficiently by moving 10% faster and carrying 25% more resources."
    self.research_time = 75

def research_hand_cart(self):
    self.name = "Hand Cart"
    self.cost = {"Food": 300, "Wood": 200}
    self.explanation_text = "Villagers work more efficiently by moving 10% faster and carrying 50% more resources."
    self.research_time = 55

def research_town_watch(self):
    self.name = "Town Watch"
    self.cost = {"Food": 75}
    self.explanation_text = "Increases the line of sight of all buildings by +4 so they see enemies from a longer distance."
    self.research_time = 25

def research_town_patrol(self):
    self.name = "Town Patrol"
    self.cost = {"Food": 300, "Gold": 100}
    self.explanation_text = "Increases the line of sight of all buildings by +4 so they see enemies from a longer distance."
    self.research_time = 40


#### Monastery
def research_redemption(self):
    self.name = "Redemption"
    self.cost = {"Gold": 475}
    self.explanation_text = "Monks can convert enemy buildings (except Town Centers, Castles, Monasteries, Farms, Fish Traps, walls, Gates, and Wonders) and siege weapons. Monks can convert most enemy units from a distance, but they must stand adjacent to buildings, rams, and Trebuchets to convert them."
    self.research_time = 50

def research_atonement(self):
    self.name = "Atonement"
    self.cost = {"Gold": 325}
    self.explanation_text = "Monks can convert enemy Monks."
    self.research_time = 40

def research_herbal_medicine(self):
    self.name = "Herbal Medicine"
    self.cost = {"Gold": 200}
    self.explanation_text = "Units garrisoned in buildings heal 6X faster."
    self.research_time = 35

def research_heresy(self):
    self.name = "Heresy"
    self.cost = {"Gold": 1000}
    self.explanation_text = "Units converted by an enemy Monk (or Missionary) die instead of changing to the enemy's color."
    self.research_time = 60

def research_sanctity(self):
    self.name = "Sanctity"
    self.cost = {"Gold": 120}
    self.explanation_text = "Monks have +15 hit points so they are harder to kill."
    self.research_time = 60

def research_fervor(self):
    self.name = "Fervor"
    self.cost = {"Gold": 140}
    self.explanation_text = "Monks move 15% faster."
    self.research_time = 50

def research_faith(self):
    self.name = "Faith"
    self.cost = {"Food": 750, "Gold": 1000}
    self.explanation_text = "Units are 50% harder for enemy Monks to convert."
    self.research_time = 60

def research_illumination(self):
    self.name = "Illumination"
    self.cost = {"Gold": 120}
    self.explanation_text = "Monks regain their faith 50% faster after a successful conversion."

def research_block_printing(self):
    self.name = "Block Printing"
    self.cost = {"Gold": 200}
    self.explanation_text = "Monks have +3 conversion range."
    self.research_time = 55

def research_theocracy(self):
    self.name = "Theocracy"
    self.cost = {"Gold": 200}
    self.explanation_text = "If a group of Monks converts an enemy unit, only one of the Monks must rest afterward."
    self.research_time = 75

#### Market

# Tribute Fees
def research_coinage(self):
    self.name = "Coinage"
    self.cost = {"Food": 200, "Gold": 100}
    self.explanation_text = "Reduces fee for tributes to 20%."
    self.research_time = 70

def research_banking(self):
    self.name = "Banking"
    self.cost = {"Food": 300, "Gold": 200}
    self.explanation_text = "Tributes are free."
    self.research_time = 70

# Trade Cart upgrades
def research_caravan(self):
    self.name = "Caravan"
    self.cost = {"Food": 200, "Gold": 200}
    self.explanation_text = "Trade Carts and Trade Cogs move 50% faster (so gold accumulates faster)."
    self.research_time = 40

# Trading Fees
def research_guilds(self):
    self.name = "Guilds"
    self.cost = {"Food": 300, "Gold": 200}
    self.explanation_text = "Reduces the commodity trading fee to 15%."
    self.research_time = 50

#### University

# Building HP upgrades
def research_masonry(self):
    self.name = "Masonry"
    self.cost = {"Food": 150, "Wood": 175}
    self.explanation_text = "Strengthens all buildings by providing 10% more hit points, +1 normal/+1 pierce armor, and +3 building armor."
    self.research_time = 70

def research_architecture(self):
    self.name = "Architecture"
    self.cost = {"Food": 300, "Wood": 200}
    self.explanation_text = "Strengthens all buildings by providing 10% more hit points, +1 normal/+1 pierce armor, and +3 building armor."
    self.research_time = 70

def research_fortified_wall(self):
    self.name = "Fortified Wall"
    self.cost = {"Food": 200, "Wood": 100}
    self.explanation_text = "Upgrades your Stone Walls and lets you build Fortified Walls, which are stronger and harder to breach. Also increases the hit points of your Gates, which makes them harder to destroy."
    self.research_time = 50

# Tower upgrades
def research_guard_tower(self):
    self.name = "Guard Tower"
    self.cost = {"Food": 100, "Wood": 250}
    self.explanation_text = "Upgrades your Watch Towers and lets you build Guard Towers, which are stronger and have more attack strength."
    self.research_time = 30

def research_keep(self):
    self.name = "Keep"
    self.cost = {"Food": 500, "Wood": 350}
    self.explanation_text = "Upgrades Guard Towers and lets you build Keeps, which are stronger and have more attack strength, range, and armor."
    self.research_time = 75

def research_treadmill_crane(self):
    self.name = "Treadmill Crane"
    self.cost = {"Food": 300, "Wood": 200}
    self.explanation_text = "Villagers construct buildings 20% faster."
    self.research_time = 50

def research_murder_holes(self):
    self.name = "Murder Holes"
    self.cost = {"Food": 200, "Stone": 100}
    self.explanation_text = "Eliminates the minimum range of all towers, Castles and Harbors so they can fire at enemies attacking their base."
    self.research_time = 60

def research_ballistics(self):
    self.name = "Ballistics"
    self.cost = {"Wood": 300, "Gold": 175}
    self.explanation_text = "Archers, Town Centers, Castles, Galleys, Unique Naval Units, and Mounted Archers fire more accurately at moving targets."
    self.research_time = 60

def research_chemistry(self):
    self.name = "Chemistry"
    self.cost = {"Food": 300, "Gold": 200}
    self.explanation_text = "Missile units (except gunpowder units) have +1 attack strength."
    self.research_time = 100

def research_siege_engineers(self):
    self.name = "Siege Engineers"
    self.cost = {"Food": 500, "Wood": 600}
    self.explanation_text = "Siege weapons have +1 range (except rams and Armored Elephants) and cause 20% more damage to buildings (40% more for Petards)."
    self.research_time = 45

def research_arrowslits(self):
    self.name = "Arrowslits"
    self.cost = {"Food": 250, "Wood": 250}
    self.explanation_text = "Increases the attack of towers and Donjons."
    self.research_time = 25

def research_bombard_tower(self):
    self.name = "Bombard Tower"
    self.cost = {"Food": 800, "Wood": 400}
    self.explanation_text = "Lets you build Bombard Towers, which are powerful and have extensive line of sight."
    self.research_time = 60

def research_heated_shot(self):
    self.name = "Heated Shot"
    self.cost = {"Food": 350, "Gold": 100}
    self.explanation_text = "Towers cause 125% more damage to ships; Castles cause 25% more damage to ships."
    self.research_time = 30
