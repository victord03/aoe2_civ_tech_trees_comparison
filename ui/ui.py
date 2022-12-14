from classes.Civilization import Civilization

# Display

NL = "\n"


def display_class_buildings(civilization: Civilization):

    print()

    for index, outer_key in enumerate(civilization.buildings):
        building_key = civilization.buildings[outer_key]
        cost_list = [f"{cost} {resource}" for resource, cost in building_key.cost.items()]
        print(f"{index}: {building_key.name} ({', '.join(cost_list)})")

    print()
