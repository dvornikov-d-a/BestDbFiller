class Entity(object):
    def __init__(self, name='NULL', hp='NULL', hits='NULL', danger='NULL', desc='NULL', exp='NULL',
                 stats='NULL', armor='NULL'):
        self.name = name
        self.hp = hp
        self.hits = hits
        self.danger = danger
        self.desc = desc
        self.exp = exp
        self.stats = stats
        self.armor = armor

    def __repr__(self):
        return "Entity('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', )" \
               % (self.name, self.hp, self.hits, self.danger, self.desc, self.exp, self.stats, self.armor)
