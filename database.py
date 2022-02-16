from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/inventor_db")
Base = declarative_base()

class Good(Base):
    __tablename__ = 'Good'

    id = Column(Integer, Sequence('good_id_seq'), primary_key=True)
    name = Column(String(255), nullable=False)

Base.metadata.create_all(engine)