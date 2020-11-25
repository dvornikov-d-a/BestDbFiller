class EntityAction(object):
    def __init__(self, entity, active_action):
        self.entity = entity
        self.active_action = active_action

    def __repr__(self):
        return "EntityAction('%s', '%s')" % (self.entity, self.active_action)
