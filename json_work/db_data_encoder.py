from json import JSONEncoder

from json_work.models.db_data import DbData


class DbDataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
