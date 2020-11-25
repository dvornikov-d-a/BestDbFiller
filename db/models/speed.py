class EntitySpeed(object):
    def __init__(self, entity, speed_type, speed_value):
        self.entity = entity
        self.speed_type = speed_type
        self.speed_value = speed_value

    def __repr__(self):
        return "EntitySpeed('%s', '%s', '%s')" % (self.entity, self.speed_type, self.speed_value)
