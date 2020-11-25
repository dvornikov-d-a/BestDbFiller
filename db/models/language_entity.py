class EntityLanguage(object):
    def __init__(self, entity, language):
        self.entity = entity
        self.language = language

    def __repr__(self):
        return "EntityLanguage('%s', '%s')" % (self.entity, self.language)
