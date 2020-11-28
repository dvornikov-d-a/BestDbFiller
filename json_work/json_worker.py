import json
import copy
import os.path

from db.models.ability import Ability
from db.models.active_action import ActiveAction
from db.models.armor import Armor
from db.models.entity import Entity
from db.models.feeling import Feeling
from db.models.language import Language
from db.models.skill import Skill
from db.models.speed import Speed
from db.models.stat import Stat
from json_work.db_data_encoder import DbDataEncoder
from json_work.models.db_data import DbData
from json_work.models.monster import Monster


class JsonWorker(object):
    def __init__(self):
        self.db_data_path = 'json_work/json_source/db_data.json'
        self.monsters_path = 'json_work/json_source/monsters.json'
        self.monsters_list = []
        self.db_data = DbData()

    def get_db_data(self):
        self.db_data.clear()

        def decode_object(o):
            o_dict = o
            if 'db_data' in o_dict and isinstance(o_dict['db_data'], bool):
                db_data = DbData()
                o_dict.pop('db_data')
                db_data.__dict__.update(o_dict)
                return db_data
            elif 'ability' in o_dict and isinstance(o_dict['ability'], bool):
                ability = Ability()
                o_dict.pop('ability')
                ability.__dict__.update(o_dict)
                return ability
            elif 'active_action' in o_dict and isinstance(o_dict['active_action'], bool):
                active_action = ActiveAction()
                o_dict.pop('active_action')
                active_action.__dict__.update(o_dict)
                return active_action
            elif 'armor' in o_dict and isinstance(o_dict['armor'], bool):
                armor = Armor()
                o_dict.pop('armor')
                armor.__dict__.update(o_dict)
                return armor
            elif 'entity' in o_dict and isinstance(o_dict['entity'], bool):
                entity = Entity()
                o_dict.pop('entity')
                entity.__dict__.update(o_dict)
                return entity
            elif 'feeling' in o_dict and isinstance(o_dict['feeling'], bool):
                feeling = Feeling()
                o_dict.pop('feeling')
                feeling.__dict__.update(o_dict)
                return feeling
            elif 'language' in o_dict and isinstance(o_dict['language'], bool):
                language = Language()
                o_dict.pop('language')
                language.__dict__.update(o_dict)
                return language
            elif 'skill' in o_dict and isinstance(o_dict['skill'], bool):
                skill = Skill()
                o_dict.pop('skill')
                skill.__dict__.update(o_dict)
                return skill
            elif 'speed' in o_dict and isinstance(o_dict['speed'], bool):
                speed = Speed()
                o_dict.pop('speed')
                speed.__dict__.update(o_dict)
                return speed
            elif 'stat' in o_dict and isinstance(o_dict['stat'], bool):
                stat = Stat()
                o_dict.pop('stat')
                stat.__dict__.update(o_dict)
                return stat
            return o

        with open(self.db_data_path, 'r', encoding='utf8') as json_file:
            self.db_data = json.load(json_file, object_hook=decode_object)
        return copy.deepcopy(self.db_data)

    def serialize_db_data(self):
        self._parse_monsters()
        with open(self.db_data_path, 'w', encoding='utf8') as json_file:
            json.dump(self.db_data, json_file, cls=DbDataEncoder, indent=4, ensure_ascii=False)

    def _parse_monsters(self):
        self._deserialize_monsters()
        for monster in self.monsters_list:
            self._parse_abilities(monster.abilities)
            self._parse_active_actions(monster.actions)
            self._parse_armor(monster.armor_class)
            self._parse_entity(monster)
            self._parse_feelings(monster.feelings)
            # self._parse_languages(?)
            self._parse_skills(monster.skills)
            self._parse_speed(monster.speed)
            self._parse_stats(monster)

    def _deserialize_monsters(self):
        self.monsters_list.clear()
        with open(self.monsters_path, 'r', encoding='utf8') as json_file:
            monsters_dicts = json.load(json_file)
        for monster_dict in monsters_dicts:
            if 'name' in monster_dict.keys():
                name = monster_dict['name']
            else:
                name = ''
            if 'armor_class' in monster_dict.keys():
                armor_class = monster_dict['armor_class']
            else:
                armor_class = ''
            if 'hits' in monster_dict.keys():
                hits = monster_dict['hits']
            else:
                hits = ''
            if 'speed' in monster_dict.keys():
                speed = monster_dict['speed']
            else:
                speed = ''
            if 'strength' in monster_dict.keys():
                strength = monster_dict['strength']
            else:
                strength = ''
            if 'agility' in monster_dict.keys():
                agility = monster_dict['agility']
            else:
                agility = ''
            if 'physique' in monster_dict.keys():
                physique = monster_dict['physique']
            else:
                physique = ''
            if 'intellect' in monster_dict.keys():
                intellect = monster_dict['intellect']
            else:
                intellect = ''
            if 'wisdom' in monster_dict.keys():
                wisdom = monster_dict['wisdom']
            else:
                wisdom = ''
            if 'charisma' in monster_dict.keys():
                charisma = monster_dict['charisma']
            else:
                charisma = ''
            if 'skills' in monster_dict.keys():
                skills = monster_dict['skills']
            else:
                skills = ''
            if 'feelings' in monster_dict.keys():
                feelings = monster_dict['feelings']
            else:
                feelings = ''
            if 'danger' in monster_dict.keys():
                danger = monster_dict['danger']
            else:
                danger = ''
            if 'abilities' in monster_dict.keys():
                abilities = monster_dict['abilities']
            else:
                abilities = ''
            if 'is_player' in monster_dict.keys():
                is_player = monster_dict['is_player']
            else:
                is_player = ''
            if 'actions' in monster_dict.keys():
                actions = monster_dict['actions']
            else:
                actions = ''
            if 'description' in monster_dict.keys():
                description = monster_dict['description']
            else:
                description = ''
            monster = Monster(name, armor_class, hits, speed, strength, agility, physique, intellect, wisdom,
                              charisma, skills, feelings, danger, abilities, is_player, actions, description)
            self.monsters_list.append(monster)

    def _parse_abilities(self, abilities_str):
        pass

    def _parse_active_actions(self, active_actions_str):
        pass

    def _parse_armor(self, armor_str):
        armor = Armor()

        class_char = armor_str.strip().split('(')
        if any(class_char):
            armor_class = class_char[0].strip()
            armor.class_ = armor_class
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
                armor.extra = ', '.join(extras)

        self.db_data.armors.append(armor)

    def _parse_entity(self, monster):
        name = monster.name.strip()
        hits = monster.hits.strip()
        danger_exp = tuple([danger_or_exp.strip() for danger_or_exp in monster.danger.strip().split('-')])
        if len(danger_exp) == 2:
            danger = danger_exp[0]
            exp = danger_exp[1]
        else:
            danger = 'NULL'
            exp = 'NULL'
        desc = monster.description.strip()
        entity = Entity(name=name, hits=hits, danger=danger, exp=exp, desc=desc)
        self.db_data.entities.append(entity)

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

        self.db_data.feelings.append(monster_feelings)

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

        self.db_data.skills.append(monster_skills)

    def _parse_speed(self, speeds_str):
        monster_speeds = []

        # избавиться от скобок
        while speeds_str.__contains__('('):
            if not speeds_str.__contains__(')'):
                self.db_data.speeds.append(monster_speeds)
                return

            open_scope_index = speeds_str.index('(')
            close_scope_index = speeds_str.index(')')
            speeds_str = speeds_str[:open_scope_index] + speeds_str[close_scope_index + 1:]

        speeds_str_list = [speed_str.strip() for speed_str in speeds_str.strip().split(',')]
        for speed_str in speeds_str_list:
            words = [word.strip() for word in speed_str.split(' ')]
            if any(words):
                speed = Speed()
                if 'фт.' in words:
                    ft_index = words.index('фт.')
                    val_index = ft_index - 1
                    value = "%s %s" % (words[val_index].replace('фт', ''), words[ft_index])
                    speed.value = value
                    if val_index != 0:
                        type_ = words[0]
                        speed.type = type_

                    monster_speeds.append(speed)

        self.db_data.speeds.append(monster_speeds)

    def _parse_stats(self, monster):
        strength, strength_plus = self._parse_stat_and_plus(monster.strength)
        physique, physique_plus = self._parse_stat_and_plus(monster.physique)
        intellect, intellect_plus = self._parse_stat_and_plus(monster.intellect)
        wisdom, wisdom_plus = self._parse_stat_and_plus(monster.wisdom)
        charisma, charisma_plus = self._parse_stat_and_plus(monster.charisma)
        stat = Stat(strength, strength_plus, physique, physique_plus, intellect, intellect_plus,
                    wisdom, wisdom_plus, charisma, charisma_plus)
        self.db_data.stats.append(stat)

    @staticmethod
    def _parse_stat_and_plus(stat_str):
        stat_and_plus = [str_.strip() for str_ in stat_str.strip().split(' ')]
        if len(stat_and_plus) == 2:
            stat = stat_and_plus[0]
            plus = stat_and_plus[1].replace('(', '').replace(')', '')
        else:
            stat, plus = 0, 0

        return stat, plus

    @staticmethod
    def _parse_int_from_str(string):
        return int(''.join([symbol for symbol in string if symbol.isdigit()]))
