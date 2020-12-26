from sqlalchemy import create_engine, MetaData
from app.settings import config
from app.db import tables, meta

dsn = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine, tbnames):
    meta.create_all(bind=engine, tables=tbnames)

if __name__ == "__main__":
    db_url = dsn.format(**config['postgres'])
    engine = create_engine(db_url, echo=True)
    create_tables(engine, tables)