from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Paises(Base):
    __tablename__ = 'paiss'
    id = Column(Integer, primary_key=True, index=True)
    nombre_pais = Column(String(255), nullable=False)
    mundial = relationship('Mundiales', back_populates='pais', cascade='all, delete-orphan')

class Mundiales(Base):
    __tablename__ = 'mundial'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    pais_id = Column(Integer, ForeignKey('paiss.id'))
    pais = relationship('Paises', back_populates='mundial')