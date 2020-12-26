from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, Date, Text, ForeignKey
import aiopg.sa
import asyncio

meta = MetaData()

posts = Table(
    'post', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(100), nullable=False),
    Column('text', Text, nullable=True),
    Column('pub_date', Date, nullable=False),
    Column('tagID', ForeignKey('tag.id'), nullable=True)
)

tags = Table(
    'tag', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(100), nullable=False),
    Column('pub_date', Date, nullable=False)
)
tables = [posts, tags]


async def get_post(post_id, conn):
    post = posts.select().where(posts.c.id==post_id)
    cursor = await conn.execute(post)
    return cursor


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database = conf['database'],
        user = conf['user'],
        password = conf['password'],
        host = conf['host'],
        port = conf['port'],
        minsize = conf['minsize'],
        maxsize = conf['maxsize']
    )
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


