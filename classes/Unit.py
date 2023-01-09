
class Unit:
    """Unit class.

    Handles all Unit data.
    """

    name: str
    cost: dict
    hp: int
    attack: int
    armor: int
    pierce_armor: int
    range: float
    minimum_range: int
    line_of_sight: int
    garrison: int
    explanation_text: str
    build_time: int
    # todo: think about a 'requirements: list' attribute

    def __init__(self, data_dict: dict):
        """Init method.

        Copies data from parameter 'data_dict' unto class. Expects the exact key names, as the class attributes."""

        self.name = data_dict["Name"]
        self.cost = data_dict["Cost"]
        self.hp = data_dict["HP"]
        self.attack = data_dict["Attack"]
        self.armor = data_dict["Armor"]
        self.pierce_armor = data_dict["Pierce Armor"]
        self.range = data_dict["Range"]
        self.minimum_range = data_dict["Minimum Range"]
        self.line_of_sight = data_dict["Line of Sight"]
        self.garrison = data_dict["Garrison"]
        self.explanation_text = data_dict["Explanation Text"]
        self.build_time = data_dict["Build Time"]
