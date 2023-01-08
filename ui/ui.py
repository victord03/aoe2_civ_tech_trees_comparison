from classes.Civilization import Civilization

NL = "\n"


# Display
def display_class_buildings(civilization: Civilization):
    """Displays all buildings of a Civilization class.

    It loops through the civlization 'buildings' attribute, and using enumerate can display an index for better
    readability.

    It finally shows the name and the cost (per resource) of each building."""

    print()

    for index, outer_key in enumerate(civilization.buildings):
        building_key = civilization.buildings[outer_key]
        cost_list = [f"{cost} {resource}" for resource, cost in building_key.cost.items()]
        print(f"{index}: {building_key.name} ({', '.join(cost_list)})")

    print()
