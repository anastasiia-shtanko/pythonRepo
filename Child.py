import Parent


class Child(Parent):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def __count(self):
        chtemp = super().currDate()
        return chtemp.year()-self.age

    def birthYear(self):
        print("Birth year: ", self.__count())

    def show(self):
        print("Name: ", self.name, ",")
        print("Age: ", self.age, " years,")
        print("Height: ", self.height, " sm.")

