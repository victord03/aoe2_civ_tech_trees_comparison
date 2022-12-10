from classes.tech_tree import TechTree


def main():

    teutons_not_available_techs = [
        "Eagle Scout",
        "Eagle Warrior",
        "Elite Eagle warrior",
        "Arbalester",
        "Heavy Cavalry Archer",
        "Thumb Ring",
        "Parthian Tactics",
        "Light Cavalry",
        "Hussar",
        "Camel Rider",
        "Heavy Camel Rider",
        "Husbandry",
        "Bracer",
        "Siege Ram",
        "Elite Cannon Galleon",
        "Dry Dock",
        "Shipwright",
        "Architecture",
        "Treadmill Crane",
        "Gold Shaft Mining",
    ]

    Teutons = TechTree(teutons_not_available_techs)
    print(Teutons.civ_tree.items())


if __name__ == "__main__":
    main()
