from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, VARCHAR, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql+psycopg2://postgres:LuckyStrike@localhost/postgres', echo=True)
#
# conn = engine.connect()
# conn.execute('COMMIT')
# conn.execute('CREATE DATABASE test_db')
# conn.close()

# Соединение с БД
engine = create_engine('postgresql+psycopg2://postgres:LuckyStrike@localhost/test_db', echo=True)

# Создание таблицы в БД
metadata = MetaData()
test_table = Table('stats', metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True),
                   Column('name', VARCHAR(60), nullable=True),
                   Column('age', Integer, nullable=True),
                   )
metadata.create_all(bind=engine)


# Определение класса для отображения в таблицу
class Stat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Stat('%s', '%s')>" % (self.name, self.age)


# Настройка отображения
mapper(Stat, test_table)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление нового объекта
stat = Stat('Dima', 21)
session.add(stat)

# Сохранение изменений
session.commit()
