import json

from json_work import monster
from db.models.armor import Armor


class JsonWorker(object):
    def __init__(self):
        self.monsters_path = 'monsters.json'
        self.monsters_list = []

        self.abilities = []
        self.active_actions = []
        self.armors = []
        self.entities = []
        self.entities_abilities = []
        self.entities_actions = []
        self.entities_feelings = []
        self.entities_languages = []
        self.entities_skills = []
        self.feelings = []
        self.languages = []
        self.skills = []
        self.speeds = []
        self.stats = []

    def parse_monsters(self):
        self._deserialize_monsters()
        for monster in self.monsters_list:
            pass
        pass

    def _deserialize_monsters(self):
        with open(self.monsters_path, 'r', encoding='utf8') as json_file:
            self.monsters_list = json.load(json_file)

    def _parse_abilities(self, abilities_str):
        pass

    def _parse_active_actions(self, active_actions_str):
        pass

    def _parse_armor(self, armor_str):
        armor = Armor()

        class_char = armor_str.strip().split('(')
        if any(class_char):
            armor_class = class_char[0].strip()
            armor.armor_class = armor_class
        if len(class_char) == 2:
            types_extras_str = class_char[1].strip().replace(')', '')
            types_extras = types_extras_str.split(',')
            types_extras = [type_extra.strip() for type_extra in types_extras]
            types = []
            extras = []
            for type_extra in types_extras:
                if any(map(str.isdigit, type_extra)):
                    extras.append(type_extra)
                else:
                    types.append(type_extra)
            if any(types):
                armor.type = ', '.join(types)
            if any(extras):
                armor.extra_armor = ', '.join(extras)




    def _parse_entity(self, monster):
        pass

    def _parse_feelings(self, feelings_str):
        pass

    def _parse_skills(self, skills_str):
        pass

    def _parse_speed(self, speed_str):
        pass

    def _parse_stats(self, stats_str):
        pass

