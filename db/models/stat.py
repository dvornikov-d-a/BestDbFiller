from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Stat(object, Base):
    # __tablename__ = 'stats'
    # id = Column('id', Integer, primary_key=True)
    # strength = Column('strength', Integer)
    # strength_plus = Column('strength_plus', Integer)
    # physique = Column('physique', Integer)
    # physique_plus = Column('physique_plus', Integer)
    # intellect = Column('intellect', Integer)
    # intellect_plus = Column('intellect_plus', Integer)
    # wisdom = Column('wisdom', Integer)
    # wisdom_plus = Column('wisdom_plus', Integer)
    # charisma = Column('charisma', Integer)
    # charisma_plus = Column('charisma_plus', Integer)

    def __init__(self, strength='NULL', strength_plus='NULL', physique='NULL', physique_plus='NULL',
                 intellect='NULL', intellect_plus='NULL', wisdom='NULL', wisdom_plus='NULL',
                 charisma='NULL', charisma_plus='NULL'):
        self.strength = strength
        self.strength_plus = strength_plus
        self.physique = physique
        self.physique_plus = physique_plus
        self.intellect = intellect
        self.intellect_plus = intellect_plus
        self.wisdom = wisdom
        self.wisdom_plus = wisdom_plus
        self.charisma = charisma
        self.charisma_plus = charisma_plus

    def __repr__(self):
        return "<Stat('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.strength,
                                                                                       self.strength_plus,
                                                                                       self.physique,
                                                                                       self.physique_plus,
                                                                                       self.intellect,
                                                                                       self.intellect_plus,
                                                                                       self.wisdom,
                                                                                       self.wisdom_plus,
                                                                                       self.charisma,
                                                                                       self.charisma_plus)

