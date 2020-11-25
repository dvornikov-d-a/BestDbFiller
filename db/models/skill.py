class Skill(object):
    def __init__(self, name, buff):
        self.name = name
        self.buff = buff

    def __repr__(self):
        return "Skill('%s', '%s')" % (self.name, self.buff)
