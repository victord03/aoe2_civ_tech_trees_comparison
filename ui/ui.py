from classes.Civ import Civ

# display

NL = "\n"


def display_class_buildings(civilization: Civ):

    print()

    for index, each_building in enumerate(civilization.buildings):

        cost_list = list()

        for resource, cost in each_building.cost.items():
            cost_list.append(f"{cost} {resource}")

        print(
            f"{index}: {each_building.name} ({', '.join(cost_list)})"
        )

    print()
