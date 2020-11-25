class Feeling(object):
    def __init__(self, name, buff, radius):
        self.name = name
        self.buff = buff
        self.radius = radius

    def __repr__(self):
        return "Feeling('%s', '%s', '%s')" % (self.name, self.buff, self.radius)
