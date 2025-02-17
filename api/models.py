from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ElektrikModel(Base):
  __tablename__ = 'elektrik'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255))
  price = Column(Float)


class SantexnikaModel(Base):
  __tablename__ = 'santexnika'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255))
  price = Column(Float)


class XirdavatModel(Base):
  __tablename__ = 'xirdavat'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255))
  price = Column(Float)


class IstilikVeHavalandirmaModel(Base):
  __tablename__ = 'istilik_ve_havalandirma'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255))
  price = Column(Float)