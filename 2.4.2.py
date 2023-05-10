class BigThing():
    def __init__(self, var):
        self.var = var

    def size(self):
        if str(self.var).isnumeric():
            return self.var
        elif isinstance(self.var, list) or isinstance(self.var, str) or isinstance(self.var, dict):
            return len(self.var)


class BigCat(BigThing):
    def __init__(self, name, weight):
        BigThing.__init__(self, name)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        if self.weight > 15:
            return "Fat"
        return "OK"


my_thing = BigThing("balloon")
print(my_thing.size())
cutie = BigCat("mitzy", 22)
print(cutie.size())
