from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph 
from sqlalchemy.engine.url import URL
from sqlalchemy import MetaData

# meta = MetaData('postgres://postgres:admin123@127.0.0.1:5432/test')

# db_url = {
#          'drivername': 'postgres',
#           'username': 'postgres',
#           'password': '***',
#           'host': 'localhost',
#         'database': "test_db",
#           'port': 5432}
# engine = create_engine(URL(**db_url))

# create the pydot graph object by autoloading all tables via a bound metadata object'
meta = MetaData('postgresql://postgres:admin123@localhost/test')
graph = create_schema_graph(metadata=meta,
    show_datatypes=False, # The image would get nasty big if we'd show the datatypes
    show_indexes=False, # ditto for indexes
    rankdir='LR', # From left to right (instead of top to bottom)
    concentrate=False # Don't try to join the relation lines together
)
graph.write_png('erd.png') # write out the file

# from sqlalchemy import create_engine, inspect
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.engine.url import URL
# from sqlalchemy import MetaData

# db_url = {
#           'drivername': 'postgres',
#           'username': 'postgres',
#           'password': 'admin123',
#           'host': 'localhost',
#           'database': "test",
#           'port': 5432}
# engine = create_engine(URL(**db_url))
# session_obj = sessionmaker(bind=engine)
# meta = MetaData()
# meta.reflect(bind=engine)
# user_t= meta.tables.get('articles')
# sel_st = user_t.select()
# conn = engine.connect()
# res = conn.execute(sel_st)
# for _row in res:
#     print(_row)