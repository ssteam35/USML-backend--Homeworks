
class Competition:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, distance: int):
        self.distance = distance


    def get_distance_range(self):
        return range(self.distance)