from ui import ui
from classes.Civilization import Civilization


def main():

    a_civ = Civilization()
    a_civ.create_civ_baseline()

    ui.display_class_buildings(a_civ)


if __name__ == "__main__":
    main()
