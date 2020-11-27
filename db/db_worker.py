from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, mapper

from db.db_config import *
from json_work.models.db_data import DbData


class DbWorker(object):
    def __init__(self):
        connection_str = 'postgresql+psycopg2://{}:{}@{}/{}'.format(username, password, host, db_name)
        self.engine = create_engine(connection_str, echo=True)
        # self.session = sessionmaker(bind=self.engine)()
        # self.metadata = MetaData(bind=self.engine)

    def insert_db_data(self, db_data):
        with self.engine.connect() as connection:
            stats_ids = self._insert_stats(db_data.stats, connection)
            abilities_ids = self._insert_abilities(db_data.abilities, connection)
            languages_ids = self._insert_languages(db_data.languages, connection)
            active_actions_ids = self._insert_active_actions(db_data.active_actions, connection)
            armors_ids = self._insert_armors(db_data.armors, connection)
            skills_ids = self._insert_skills(db_data.skills, connection)
            feelings_ids = self._insert_feelings(db_data.feelings, connection)
            entities_ids = self._insert_entities(db_data.entities, stats_ids, armors_ids, connection)
            speeds_ids = self.__insert_speeds(db_data.speeds, entities_ids, connection)

    def _insert_stats(self, stats, connection):
        stats_ids = []
        for monster_stat in stats:
            strength = self._parse_int_from_str(monster_stat.strength)
            strength_plus = self._parse_int_from_str(monster_stat.strength_plus)
            physique = self._parse_int_from_str(monster_stat.physique)
            physique_plus = self._parse_int_from_str(monster_stat.physique_plus)
            intellect = self._parse_int_from_str(monster_stat.intellect)
            intellect_plus = self._parse_int_from_str(monster_stat.intellect_plus)
            wisdom = self._parse_int_from_str(monster_stat.wisdom)
            wisdom_plus = self._parse_int_from_str(monster_stat.wisdom_plus)
            charisma = self._parse_int_from_str(monster_stat.charisma)
            charisma_plus = self._parse_int_from_str(monster_stat.charisma_plus)

            insert_query = f'INSERT INTO {stats_table_name}' \
                           f' ({stats_strength_col_name}, {stats_strength_plus_col_name},' \
                           f' {stats_physique_col_name}, {stats_physique_plus_col_name},' \
                           f' {stats_intellect_col_name}, {stats_intellect_plus_col_name},' \
                           f' {stats_wisdom_col_name}, {stats_wisdom_plus_col_name},' \
                           f' {stats_charisma_col_name}, {stats_charisma_plus_col_name}) ' \
                           f'VALUES ' \
                           f'({strength}, {strength_plus},' \
                           f' {physique}, {physique_plus},' \
                           f' {intellect}, {intellect_plus},' \
                           f' {wisdom}, {wisdom_plus},' \
                           f' {charisma}, {charisma_plus}) ' \
                           f'RETURNING id;'
            stat_id = self._insert_returning_id(insert_query, connection)
            stats_ids.append(stat_id)

            return stats_ids

    def _insert_abilities(self, abilities, connection):
        abilities_ids = []

        for monster_abilities in abilities:

            monster_abilities_ids = []

            for ability in monster_abilities:
                name = self._null_or_str(ability.name)
                info = self._null_or_str(ability.info)
                insert_query = f'INSERT INTO {abilities_table_name} ' \
                               f'({abilities_name_col_name}, {abilities_info_col_name}) ' \
                               f'VALUES ' \
                               f'({name}, {info}) ' \
                               f'RETURNING id;'
                ability_id = self._insert_returning_id(insert_query, connection)
                monster_abilities_ids.append(ability_id)

            abilities_ids.append(monster_abilities_ids)

        return abilities_ids

    def _insert_languages(self, languages, connection):
        languages_ids = []
        for monster_languages in languages:
            monster_languages_ids = []
            for language in monster_languages:
                name = self._null_or_str(languages.name)
                info = self._null_or_str(languages.info)

                insert_query = f'INSERT INTO {languages_table_name} ' \
                               f'({languages_name_col_name}, {languages_info_col_name}) ' \
                               f'VALUES ' \
                               f'({name}, {info}) ' \
                               f'RETURNING id;'
                language_id = self._insert_returning_id(insert_query, connection)
                monster_languages_ids.append(language_id)
            languages_ids.append(monster_languages_ids)
        return languages_ids

    def _insert_active_actions(self, active_actions, connection):
        active_actions_ids = []
        for monster_active_actions in active_actions:
            monster_active_actions_ids = []
            for active_action in monster_active_actions:
                name = self._null_or_str(active_action.name)
                desc = self._null_or_str(active_action.desc)
                insert_query = f'INSERT INTO {active_actions_table_name} ' \
                               f'({active_actions_name_col_name}, {active_actions_desc_col_name}) ' \
                               f'VALUES ' \
                               f'({name}, {desc}) ' \
                               f'RETURNING id;'
                active_action_id = self._insert_returning_id(insert_query, connection)
                monster_active_actions_ids.append(active_action_id)
            active_actions_ids.append(monster_active_actions_ids)
        return active_actions_ids

    def _insert_armors(self, armors, connection):
        armors_ids = []
        for armor in armors:
            class_ = self._parse_int_from_str(armor.class_)
            type_ = self._null_or_str(armor.type)
            extra = self._null_or_str(armor.extra)
            insert_query = f'INSERT INTO {armors_table_name} ' \
                           f'({armors_class_col_name}, {armors_type_col_name}, {armors_extra_col_name}) ' \
                           f'VALUES ' \
                           f'({class_}, {type_}, {extra}) ' \
                           f'RETURNING id;'
            armor_id = self._insert_returning_id(insert_query, connection)
            armors_ids.append(armor_id)
        return armors_ids

    def _insert_skills(self, skills, connection):
        skills_ids = []
        for monster_skills in skills:
            monster_skills_ids = []
            for skill in monster_skills:
                name = self._null_or_str(skill.name)
                buff = self._parse_int_from_str(skill.buff)
                insert_query = f'INSERT INTO {skills_table_name} ' \
                               f'({skills_name_col_name}, {skills_buff_col_name}) ' \
                               f'VALUES ' \
                               f'({name}, {buff}) ' \
                               f'RETURNING id;'
                skill_id = self._insert_returning_id(insert_query, connection)
                monster_skills_ids.append(skill_id)
            skills_ids.append(monster_skills_ids)
        return skills_ids

    def _insert_feelings(self, feelings, connection):
        feelings_ids = []
        for monster_feelings in feelings:
            monster_feelings_ids = []
            for feeling in monster_feelings:
                name = self._null_or_str(feeling.name)
                buff = self._null_or_str(feeling.buff)
                if feeling.radius != 'NULL':
                    radius = self._parse_int_from_str(feeling.radius)
                else:
                    radius = feeling.radius
                insert_query = f'INSERT INTO {feelings_table_name} ' \
                               f'({feelings_name_col_name}, {feelings_buff_col_name}, {feelings_radius_col_name}) ' \
                               f'VALUES ' \
                               f'({name}, {buff}, {radius}) ' \
                               f'RETURNING id;'
                feeling_id = self._insert_returning_id(insert_query, connection)
                monster_feelings_ids.append(feeling_id)
            feelings_ids.append(monster_feelings_ids)
        return feelings_ids

    def _insert_entities(self, entities, stats_ids, armors_ids, connection):
        entities_ids = []
        for index, entity in zip(range(len(entities)), entities):
            name = self._null_or_str(entity.name)
            hp = self._null_or_int(entity.hp)
            hits = self._null_or_str(entity.hits)
            danger = self._null_or_str(entity.danger)
            desc = self._null_or_str(entity.desc)
            exp = self._null_or_int(entity.exp)
            stats = stats_ids[index]
            armor = armors_ids[index]
            insert_query = f'INSERT INTO {entities_table_name} ' \
                           f'({entities_name_col_name}, {entities_hp_col_name}, {entities_hits_col_name},' \
                           f' {entities_danger_col_name}, {entities_desc_col_name}, {entities_exp_col_name},' \
                           f' {entities_stats_col_name}, {entities_armor_col_name}) ' \
                           f'VALUES ' \
                           f'({name}, {hp}, {hits}, {danger}, {desc}, {exp}, {stats}, {armor}) ' \
                           f'RETURNING id;'
            entity_id = self._insert_returning_id(insert_query, connection)
            entities_ids.append(entity_id)
        return entities_ids

    def __insert_speeds(self, speeds, entities_ids, connection):
        speeds_ids = []
        for entity, monster_speeds in zip(entities_ids, speeds):
            monster_speeds_ids = []
            for speed in monster_speeds:
                type_ = self._null_or_str(speed.type)
                value = self._null_or_int(speed.value)
                insert_query = f'INSERT INTO {speeds_table_name} ' \
                               f'({speeds_entity_col_name}, {speeds_type_col_name}, {speeds_value_col_name}) ' \
                               f'VALUES ' \
                               f'({entity}, {type_}, {value}) ' \
                               f'RETURNING id;'
                speed_id = self._insert_returning_id(insert_query, connection)
                monster_speeds_ids.append(speed_id)
            speeds_ids.append(monster_speeds_ids)
        return speeds_ids

    @staticmethod
    def _insert_returning_id(insert_query, connection, id_col_name='id'):
        return connection.execute(insert_query).first()[id_col_name]

    def _null_or_int(self, string):
        if string == 'NULL':
            return string
        return self._parse_int_from_str(string)

    @staticmethod
    def _parse_int_from_str(string):
        return int(''.join([symbol for symbol in string if symbol.isdigit()]))

    @staticmethod
    def _null_or_str(string):
        if string == 'NULL':
            return string
        return f"'{string}'"
