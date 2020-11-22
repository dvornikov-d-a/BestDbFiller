from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
import test

engine = create_engine('postgresql+psycopg2://postgres:LuckyStrike@localhost/test_db')
metadata = MetaData(bind=engine)
test_table = Table('stats', metadata, autoload=True, autoload_with=engine)
print([c.name for c in test_table.columns])
