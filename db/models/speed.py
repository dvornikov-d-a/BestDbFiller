from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Speed(object, Base):
    def __init__(self, entity='NULL', speed_type='NULL', speed_value='NULL'):
        self.entity = entity
        self.type = speed_type
        self.value = speed_value

    def __repr__(self):
        return "Speed('%s', '%s', '%s')" % (self.entity, self.type, self.value)
