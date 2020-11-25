class EntityAbility(object):
    def __init__(self, entity, ability):
        self.entity = entity
        self.ability = ability

    def __repr__(self):
        return "EntityAbility('%s', '%s')" % (self.entity, self.ability)
