import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class SolarBrands(Base):
    __tablename__ = 'solar_brands'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class BrandItem(Base):
    __tablename__ = 'brand_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    initial_investment = Column(String(250))
    technology_knowhow = Column(Integer, nullable = False)
    savings = Column(Integer, nullable = False)
    payback = Column(String(8))
    irr = Column(Integer, nullable = False)
    solar_brands_id = Column(Integer,ForeignKey('solar_brands.id'))
    solar_brands = relationship(SolarBrands)


engine = create_engine('sqlite:///solarbrandsmenu.db')
Base.metadata.create_all(engine)
