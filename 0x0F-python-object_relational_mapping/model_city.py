#!/usr/bin/python3
""" city model file"""

from model_state import Base
from sqlalchemy import String, Integer, Column, ForeignKey


class City(Base):
    """city model class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
