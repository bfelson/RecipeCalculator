import sqlalchemy as sqla
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

engine = sqla.create_engine('sqlite:///ingredients.db', echo=True)

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    unit = Column(String)
    cost = Column(Float)
    unit_cost = Column(Float)

Base.metadata.create_all(engine)

#Input test ingredients
flour = Ingredient(name='flour', quantity = 1, unit = "quart", cost = 5.0)

ingredients = [flour]

#Open database session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(flour)

session.commit()
