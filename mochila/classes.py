

class Item:
    def __init__(self, item_id, name, value, weight):
        self.item_id = item_id
        self.name = name
        self.name = name
        self.value = value
        self.weight = weight
        self.label = None
        self.bttn = None

class Result:
    def __init__(self):
        self.solution = []
        self.max_weight = 0