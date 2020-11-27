class Armor(object):
    def __init__(self, class_='NULL', type_='NULL', extra='NULL'):
        self.class_ = class_
        self.type = type_
        self.extra = extra

    def __repr__(self):
        return "Armor('%s', '%s', '%s')" % (self.class_, self.type, self.extra)
