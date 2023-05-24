class Animal():
    zoo_name="Hayaton"
    def __init__ (self, name, hunger=0):
        self._name=name
        self._hunger=hunger

    def get_name(self):
        return str(self._name)
    def is_hungry(self):
        if self._hunger>0:
            return True
        return False
    def feed(self):
        self._hunger-=1
    def talk(self):
        pass
    def special_methods(self):
        if isinstance(self, Dog):
            Dog.fetch_stick(self)
        elif isinstance(self, Cat):
            Cat.chase_laser(self)
        elif isinstance(self, Skunk):
            Skunk.stink(self)
        elif isinstance(self, Unicorn):
            Unicorn.sing(self)
        elif isinstance(self, Dragon):
            Dragon.breath_fire(self)

class Dog(Animal):
    def __init__ (self, name, hunger=0):
        Animal.__init__ (self, name, hunger)
    def type(self):
        return "Dog"
    def talk(self):
        print("woof woof")
    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__ (self, name, hunger=0):
        Animal.__init__ (self, name, hunger)
    def type(self):
        return "Cat"
    def talk(self):
        print("meow")
    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__ (self, name, hunger=0, _stink_count=6):
        Animal.__init__ (self, name, hunger)
    def type(self):
        return "Shunk"
    def talk(self):
        print("tssss")
    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def __init__ (self, name, hunger=0):
        Animal.__init__ (self, name, hunger)
    def type(self):
        return "Unicorn"
    def talk(self):
        print("Good day, darling")
    def sing(self):
        print("I’m not your toy...	")

class Dragon(Animal):
    def __init__ (self, name, hunger=0, _color="Green"):
        Animal.__init__ (self, name, hunger)
    def type(self):
        return "Dragon"
    def talk(self):
        print("Raaaawr")
    def breath_fire(self):
        print("$@#$#@$	")

def main():
    zoo_lst=[]
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky"))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))

    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))


    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.type() + " " + animal.get_name() )
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        animal.special_methods()
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
