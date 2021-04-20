import datetime


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def currDate(self):
        temp = datetime.datetime.now()
        print("Current date: ")
        print(temp.year, ".", temp.month, ".", temp.day)
        return temp


