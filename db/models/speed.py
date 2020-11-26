class Speed(object):
    def __init__(self, entity='NULL', speed_type='NULL', speed_value='NULL'):
        self.entity = entity
        self.type = speed_type
        self.value = speed_value

    def __repr__(self):
        return "EntitySpeed('%s', '%s', '%s')" % (self.entity, self.type, self.value)
