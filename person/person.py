class person:

    def __init__(self,name, id , age, height, weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight
    def __repr__(self):
        return repr((self.age, self.weight, self.height))
    def __str__(self):
        return "이름 : " + self.name + "  나이 : " + str(self.age) + "  키 : " + str(self.height) + "  체중 : " + str(
            self.weight)
