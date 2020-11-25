import json

from json_work import monster
from db import models


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
        pass

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

