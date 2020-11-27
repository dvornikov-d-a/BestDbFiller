class Ability(object):
    def __init__(self, name='NULL', info='NULL'):
        self.name = name
        self.info = info

    def __repr__(self):
        return "Ability('%s', '%s')" % (self.name, self.info)