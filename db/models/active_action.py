class ActiveAction(object):
    def __init__(self, name='NULL', desc='NULL'):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "ActiveAction('%s', '%s')" % (self.name, self.desc)
