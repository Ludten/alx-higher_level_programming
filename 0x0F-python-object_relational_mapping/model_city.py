#!/usr/bin/python3
"""
A module defining the state class derived from
SQLAlchemy Base instance
"""

from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from model_state import Base, State


class City(Base):
    """
    A class defining the cities table
    """
    __tablename__ = 'cities'

    id = Column(Integer,  primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)

    __table_args__ = (UniqueConstraint('id'), )
