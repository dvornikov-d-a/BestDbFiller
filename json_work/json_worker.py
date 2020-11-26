import json

from db.models.armor import Armor
from db.models.entity import Entity
from db.models.feeling import Feeling


class JsonWorker(object):
    def __init__(self):
        self.monsters_path = 'monsters.json'
        self.monsters_list = []

        self.abilities = []
        self.active_actions = []
        self.armors = []
        self.entities = []
        # self.entities_abilities = []
        # self.entities_actions = []
        # self.entities_feelings = []
        # self.entities_languages = []
        # self.entities_skills = []
        self.feelings = []  # список списков чувств монстров
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

        self.armors.append(armor)

    def _parse_entity(self, monster):
        name = monster.name.strip()
        hits = monster.hits.strip()
        danger = monster.danger.strip()
        desc = monster.description.strip()
        entity = Entity(name=name, hits=hits, danger=danger, desc=desc)
        self.entities.append(entity)

    def _parse_feelings(self, feelings_str):
        feelings_str_list = feelings_str.strip().split(',')
        feelings_str_list = [feeling_str.strip() for feeling_str in feelings_str_list]

        monster_feelings = []

        for feeling_str in feelings_str_list:
            if any(map(str.isdigit, feeling_str)):
                feeling = Feeling()

                words = [word.strip() for word in feeling_str.split(' ')]
                if words[-1].__contains__('фт') and words[-2].isdigit():
                    name = ' '.join(words[:-2])
                    radius = ' '.join(words[-2:])
                    feeling.name = name
                    feeling.radius = radius
                elif words[-1].isdigit():
                    name = ' '.join(words[:-1])
                    buff = words[-1]
                    feeling.name = name
                    feeling.buff = buff
                else:
                    continue

                monster_feelings.append(feeling)

        self.feelings.append(monster_feelings)

    def _parse_skills(self, skills_str):
        pass

    def _parse_speed(self, speed_str):
        pass

    def _parse_stats(self, stats_str):
        pass
