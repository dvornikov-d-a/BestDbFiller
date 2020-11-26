class Skill(object):
    def __init__(self, name='NULL', buff='NULL'):
        self.name = name
        self.buff = buff

    def __repr__(self):
        return "Skill('%s', '%s')" % (self.name, self.buff)
