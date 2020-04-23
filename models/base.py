from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from sqlalchemy import create_engine

# Declaring base used to create tables
Base = declarative_base()


