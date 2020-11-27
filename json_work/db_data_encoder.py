from json import JSONEncoder

from db.models.ability import Ability
from db.models.active_action import ActiveAction
from db.models.armor import Armor
from db.models.entity import Entity
from db.models.feeling import Feeling
from db.models.language import Language
from db.models.skill import Skill
from db.models.speed import Speed
from db.models.stat import Stat
from json_work.models.db_data import DbData


class DbDataEncoder(JSONEncoder):
    def default(self, o):
        o_dict = o.__dict__
        if isinstance(o, DbData):
            o_dict['db_data'] = True
        elif isinstance(o, Ability):
            o_dict['ability'] = True
        elif isinstance(o, ActiveAction):
            o_dict['active_action'] = True
        elif isinstance(o, Armor):
            o_dict['armor'] = True
        elif isinstance(o, Entity):
            o_dict['entity'] = True
        elif isinstance(o, Feeling):
            o_dict['feeling'] = True
        elif isinstance(o, Language):
            o_dict['language'] = True
        elif isinstance(o, Skill):
            o_dict['skill'] = True
        elif isinstance(o, Speed):
            o_dict['speed'] = True
        elif isinstance(o, Stat):
            o_dict['stat'] = True
        return o_dict
