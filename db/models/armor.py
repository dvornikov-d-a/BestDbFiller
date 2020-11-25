class Armor(object):
    def __init__(self, armor_class='NULL', type_='NULL', extra_armor='NULL'):
        self.armor_class = armor_class
        self.type = type_
        self.extra_armor = extra_armor

    def __repr__(self):
        return "Armor('%s', '%s', '%s')" % (self.armor_class, self.type, self.extra_armor)
