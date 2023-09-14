#!/usr/bin/python3
"""
Module that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()

engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): The primary key of the state record (auto-incremented).
        name (str): The name of the state (maximum 128 characters).
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
