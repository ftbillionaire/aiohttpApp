from sqlalchemy import Table, Column, Integer, String, Date, MetaData
from sqlalchemy import create_engine, text, update
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@db/blog', echo=True)
"""
Alchemy core
"""
meta = MetaData()

posts = Table(
    'posts', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(100), nullable=True),
    Column('pub_date', Date, nullable=False),
)

meta.create_all(engine)

# print(engine.table_names())
# print('--------')
# print(engine.driver)

## INSERT
# data = posts.insert().values(title="7 post", pub_date="2020-12-19")
# conn = engine.connect()
# result = conn.execute(data)
# print(result.inserted_primary_key)

## many inserts can be executed by following expression:
## engine.execute(posts.insert, [{*data}, {*data}, ...])

## SELECT 

# t = text("SELECT * FROM posts")
# result = conn.execute(t)
# select = posts.select().where(posts.c.id == 1)
# result = conn.execute(select)
# print(result.fetchone()) 
# for row in result:
#     print(row.id, '-', row.title, '-', row.pub_date)

## UPDATE

conn = engine.connect()
# t = text("UPDATE posts SET title='4 changed' WHERE id=4")
# stupd = update(posts).where(posts.c.id==4).values(title="4 Changed")
# conn.execute(t)

select = posts.select().order_by(posts.c.id)
result = conn.execute(select)
for row in result:
    print(row)

## DELETE 

# conn = engine.connect()
# postdel = posts.delete().where(posts.c.id == 5)
# conn.execute(postdel)

# data = posts.select()
# result = conn.execute(data)
# for row in result:
#     print(row)
"""
ORM 
"""

# Base = declarative_base()
# class Tag(Base):
#     __tablename__ = 'tags'
#     id = Column('id', Integer,primary_key=True, autoincrement=True)
#     title = Column('title', String(100), nullable=False)
#     pub_date = Column('pub_date', Date, nullable=False)

# Base.metadata.create_all(engine)