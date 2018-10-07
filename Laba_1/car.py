class Car:
    def __init__(self, name: str, max_speed, drag_coef, time_to_max):
        self.name = name
        self.time_to_max = time_to_max
        self.drag_coef = drag_coef
        self.max_speed = max_speed


    @property
    def get_name(self):
        return self.name

    @property
    def get_time_to_max(self):
        return self.time_to_max

    @property
    def get_drag_coef(self):
        return self.drag_coef

    @property
    def get_max_speed(self):
        return self.max_speed