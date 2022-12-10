from ui import ui
from classes.Civ import Civ


def main():

    a_civ = Civ()
    a_civ.create_civ_baseline()

    ui.display_class_buildings(a_civ)


if __name__ == "__main__":
    main()
