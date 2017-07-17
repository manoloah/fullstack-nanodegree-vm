import sys #provides a number of fucntion and variables to manipulate the python runtime environment

from sqlalchemy import
Column, ForeignKey, Integer, String, Float
#will come in handy when writing mapper

from sqlalchemy.ext.declarative import declarative_base

from sqlaclchemy.orm import relationship

from sqlalchemy import create_engine



Base = declarative_base()


class SolarSystems(Base):
    __tablename__= 'solar_systems'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)



class SystemItem(Base):
    __tablename__= 'system_item'
    BrandName = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column (String (250))
    initial_investment = Column(Integer, nullable = False)
    savings = Column(Integer, nullable = False)
    payback = Column(Integer, nullable = False)
    technology_knowhow = Column(Integer, nullable = False)
    irr = Column(Float, nullable = False)
    solar_systems_id = Column (Integer, ForeignKey('solar_systems.id')
    solarsytem = relationship(SolarSystems)

#######insert at end of file #######

engine = create_engine('sqlite:///solarsystemsmenu.db')

Base.metadata.create_all(engine)
