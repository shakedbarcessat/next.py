class UnderAge(Exception):
    def __init__ (self, age):
        self._age=age

    def __str__ (self):
        return "your age is " + str(self._age) + ", this age is under 18. you can come in " + str(18-self._age) + " more years"

    def get_age(self):
        return self._age

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print("Wrong age- less than 18, excepted above 18, got " + str(e.get_age()))

send_invitation("roni", 15)