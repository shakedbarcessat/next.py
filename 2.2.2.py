class Shark():
    def __init__(self):
        self.name = "arik"
        self.age = 3

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    shark1 = Shark()
    shark2 = Shark()
    shark1.birthday()
    print(shark1.get_age())
    print(shark2.get_age())


if __name__ == '__main__':
    main()
