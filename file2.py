from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, recipient= "Dana Ev", sender= "Eyal Ch", age=0):
        GreetingCard.__init__(self, recipient, sender)
        self._sender_age= age

    def greeting_msg(self):
        super(BirthdayCard, self).greeting_msg()
        print(" age: " +str(self._sender_age))
