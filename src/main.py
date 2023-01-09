from ui import ui
from classes.Civilization import Civilization


def main():
    """Main Func."""

    teutons = Civilization()
    teutons.create_teutons()

    for index, upgrade in enumerate(teutons.buildings["Monastery"].available_researches):
        print(
            f"{index+1}: {upgrade}"
        )

    for index, unit in enumerate(teutons.buildings["Stable"].available_units):
        print(
            f"{index+1}: {unit.name}"
        )

if __name__ == "__main__":
    main()
