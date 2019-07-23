from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print("You have rolled out :" + str(x))

my_die = Die(6)
my_die_0 = Die(10)
for number in range(10):
    my_die.roll_die()
    my_die_0.roll_die()


