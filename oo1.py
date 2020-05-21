class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)   # x--->Turtle
        self.fish = Fish(x)     # y--->Fish

    def print_num(self):
        print('pool\'s Turtlr number is %d, and Pool\'s Fish num is %d' % (self.turtle.num, self.turtle.num))

        
