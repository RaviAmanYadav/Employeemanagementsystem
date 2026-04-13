class Employee:
    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.age = age
        self.position = position

    def to_dict(self):
        self.to_dict()

    @staticmethod
    def from_dict(data):
        return Employee(**data)
