from wpath import findcaller


class Base(object):
    base_name = "base"

    @findcaller
    def __init__(self):
        super().__init__()

    def breathe(self):
        """
        呼吸
        """
        return "breathe"


class Animal(Base):
    def run(self):
        return "run"

    def walk(self):
        return "walk"

    def sleep(self):
        return "sleep"


class Fox(Base):
    age = 1

    @findcaller
    def __init__(self, father, name="aurora fox", sex="male"):
        self.name = name
        self.sex = sex
        self.actions = FoxManager()
        self.data_1 = [1, 2, 3]
        self.data_2 = (1, 2, 3)
        self.data_3 = {"1": 1, "2": 2, "3": 3}
        self.data_4 = {1, 2, 3}
        self.data_5 = "1, 2, 3"
        self.data_6 = 1
        self.data_7 = True
        self.data_8 = 1.1
        self.data_9 = 4 + 3j


class FoxManager(object):
    """
    manage fox actions:
        find_other_fox()
        drink()
        eat()
    """

    @findcaller
    def __init__(self):
        super().__init__()

    def find_other_fox(self):
        return "find_other_fox"

    def drink(self):
        return "drink water"

    def eat(self):
        return "eat meat"
