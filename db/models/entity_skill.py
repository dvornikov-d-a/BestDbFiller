class EntitySkill(object):
    def __init__(self, entity, skill):
        self.entity = entity
        self.skill = skill

    def __repr__(self):
        return "EntitySkill('%s', '%s')" % (self.entity, self.skill)
