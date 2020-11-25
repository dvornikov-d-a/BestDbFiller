class Armor(object):
    def __init__(self, armor_class, type, extra_armor):
        self.armor_class = armor_class
        self.type = type
        self.extra_armor = extra_armor

    def __repr__(self):
        return "Armor('%s', '%s', '%s')" % (self.armor_class, self.type, self.extra_armor)
