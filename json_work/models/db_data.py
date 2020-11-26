class DbData(object):
    def __init__(self, abilities=None, active_actions=None, armors=None, entities=None,
                 feelings=None, languages=None, skills=None, speeds=None, stats=None):
        if abilities is None:
            abilities = []
        if active_actions is None:
            active_actions = []
        if armors is None:
            armors = []
        if entities is None:
            entities = []
        if feelings is None:
            feelings = []
        if languages is None:
            languages = []
        if skills is None:
            skills = []
        if speeds is None:
            speeds = []
        if stats is None:
            stats = []
        self.abilities = abilities
        self.active_actions = active_actions
        self.armors = armors
        self.entities = entities
        # self.entities_abilities = []
        # self.entities_actions = []
        # self.entities_feelings = []
        # self.entities_languages = []
        # self.entities_skills = []
        self.feelings = feelings
        self.languages = languages
        self.skills = skills
        self.speeds = speeds
        self.stats = stats
