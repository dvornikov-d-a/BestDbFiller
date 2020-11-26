import json

from db.models.armor import Armor
from db.models.entity import Entity
from db.models.feeling import Feeling
from db.models.skill import Skill
from db.models.speed import Speed
from db.models.stat import Stat


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

    def _parse_languages(self, languages_str):
        pass

    def _parse_skills(self, skills_str):
        skills_str_list = [skill_str.strip() for skill_str in skills_str.strip().split(',')]

        monster_skills = []

        for skill_str in skills_str_list:
            name_buff = skill_str.split(' ')
            if len(name_buff) == 2:
                name = name_buff[0]
                buff = name_buff[1]
                skill = Skill(name, buff)
                monster_skills.append(skill)

        self.skills.append(monster_skills)

    def _parse_speed(self, speeds_str):
        monster_speeds = []

        # избавиться от скобок
        while speeds_str.__contains__('('):
            if not speeds_str.__contains__(')'):
                self.speeds.append(monster_speeds)
                return

            open_scope_index = speeds_str.index('(')
            close_scope_index = speeds_str.index(')')
            speeds_str = speeds_str[:open_scope_index] + speeds_str[close_scope_index+1:]

        speeds_str_list = [speed_str.strip() for speed_str in speeds_str.strip().split(',')]
        for speed_str in speeds_str_list:
            words = [word.strip() for word in speed_str.split(' ')]
            if any(words):
                speed = Speed()

                ft_index = words.index('фт.')
                val_index = ft_index - 1
                value = "%s %s" % (words[val_index].replace('фт', ''), words[ft_index])
                speed.value = value
                if val_index != 0:
                    type = words[0]
                    speed.type = type

                monster_speeds.append(speed)

        self.speeds.append(monster_speeds)

    def _parse_stats(self, monster):
        strength, strength_plus = self._parse_stat_and_plus(monster.strength)
        physique, physique_plus = self._parse_stat_and_plus(monster.physique)
        intellect, intellect_plus = self._parse_stat_and_plus(monster.intellect)
        wisdom, wisdom_plus = self._parse_stat_and_plus(monster.wisdow)
        charisma, charisma_plus = self._parse_stat_and_plus(monster.charisma)
        stat = Stat(strength, strength_plus, physique, physique_plus, intellect, intellect_plus,
                    wisdom, wisdom_plus, charisma, charisma_plus)
        self.stats.append(stat)

    @staticmethod
    def _parse_stat_and_plus(stat_str):
        stat_and_plus = [str.strip() for str in stat_str.strip().split(' ')]
        if len(stat_and_plus) == 2:
            stat = stat_and_plus[0]
            plus = stat_and_plus[1].replace('(', '').replace(')', '')
        else:
            stat, plus = 0, 0

        return stat, plus
