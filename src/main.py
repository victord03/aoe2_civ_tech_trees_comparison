from ui import ui
from classes.Civilization import Civilization


def main():

    teutons = Civilization()
    teutons.create_teutons()

    ui.display_class_buildings(teutons)

    for index, upgrade in enumerate(teutons.buildings["Mill"].available_researches):
        print(
            f"{index+1}: {upgrade}"
        )


if __name__ == "__main__":
    main()
