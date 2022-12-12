from classes.Civilization import Civilization

# Display

NL = "\n"


def display_class_buildings(civilization: Civilization):

    print()

    for index, each_building in enumerate(civilization.buildings):
        cost_list = [f"{cost} {resource}" for resource, cost in each_building.cost.items()]
        print(f"{index}: {each_building.name} ({', '.join(cost_list)})")

    print()
