from sqlalchemy import Column, Integer, String, JSON
from geoalchemy2 import Geometry
from .database import Base

class Tile(Base):
    __tablename__ = "tiles"

    id = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry('GEOMETRY'))
    properties = Column(JSON)
