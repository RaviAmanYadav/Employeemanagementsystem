class Employee:
    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.age = age
        self.position = position

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "position": self.position,
        }

    @staticmethod
    def from_dict(data):
        return Employee(**data)
