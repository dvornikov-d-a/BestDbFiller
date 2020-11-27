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
                name = self._null_or_value(ability.name)
                info = self._null_or_value(ability.info)
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
                name = self._null_or_value(languages.name)
                info = self._null_or_value(languages.info)

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
                name = self._null_or_value(active_action.name)
                desc = self._null_or_value(active_action.desc)
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
            type_ = self._null_or_value(armor.type)
            extra = self._null_or_value(armor.extra)
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
                name = self._null_or_value(skill.name)
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
                name = self._null_or_value(feeling.name)
                buff = self._null_or_value(feeling.buff)
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

    @staticmethod
    def _insert_returning_id(insert_query, connection, id_col_name='id'):
        return connection.execute(insert_query).first()[id_col_name]

    @staticmethod
    def _parse_int_from_str(string):
        return int(''.join([symbol for symbol in string if symbol.isdigit()]))

    @staticmethod
    def _null_or_value(string):
        if string == 'NULL':
            return string
        return f"'{string}'"
