class Shark():
    count = 0

    def __init__(self, name="arik"):
        self._name = name
        self._age = 3
        Shark.count += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    shark1 = Shark("roni")
    shark2 = Shark()
    print(shark1.get_name())
    print(shark2.get_name())
    shark1.set_name("octavio")
    print(shark1.get_name())
    print(Shark.count)


if __name__ == '__main__':
    main()
