class EntityFeeling(object):
    def __init__(self, entity, feeling):
        self.entity = entity
        self.feeling = feeling

    def __repr__(self):
        return "EntityFeeling('%s', '%s')" % (self.entity, self.feeling)
