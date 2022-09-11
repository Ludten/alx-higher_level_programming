#!/usr/bin/python3
"""
A module defining the state class derived from
SQLAlchemy Base instance
"""

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    A class defining the state table
    """
    __tablename__ = 'states'

    id = Column(Integer,  primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    __table_args__ = (UniqueConstraint('id'), )
