from classes.Civ import Civ

# display

NL = "\n"


def display_class_buildings(civilization: Civ):

    text = ""

    for index, each_building in enumerate(civilization.buildings):

        resources_needed = list(each_building.cost.keys())
        resource_and_cost = ""

        print(
            f"{NL}{index}: {each_building.name} " + text
        )

        for each in resources_needed:
            resource_and_cost += str(each_building.cost[each]) + each[0]

        print(resource_and_cost)

