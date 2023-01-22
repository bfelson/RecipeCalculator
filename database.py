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

    def __init__(self, name, quantity, unit, cost):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.cost = cost
        self.unit_cost = cost/unit

Base.metadata.create_all(engine)

#Open database session
def open_session():
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add_ingredient(ingredient):
    session = open_session()
    session.add(ingredient)
    session.commit()
    session.close()

