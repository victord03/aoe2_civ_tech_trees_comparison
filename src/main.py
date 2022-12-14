from ui import ui
from classes.Civilization import Civilization


def main():

    teutons = Civilization()

    teutons.create_civilization_baseline()
    teutons.create_teutons()
    # ui.display_class_buildings(teutons)

    for upgrade in teutons.buildings["Dock"].available_researches:
        print(
            upgrade
        )


if __name__ == "__main__":
    main()
