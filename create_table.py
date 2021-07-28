from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql://root:root@localhost/sqlalchemy', echo=False)
meta = MetaData()

teachers = Table(
    'teachers', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(200)),
    Column('lastname', String(100)),
)
meta.create_all(engine)