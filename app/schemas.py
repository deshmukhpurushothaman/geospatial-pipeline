# from pydantic import BaseModel

# class TileCreate(BaseModel):
#     geom: str  # Geometry in WKT format
#     properties: dict

#     class Config:
#         orm_mode = True

# class TileUpdate(BaseModel):
#     geom: str  # Geometry in WKT format (this field is updateable)
#     properties: dict  # Properties to be updated

#     class Config:
#         orm_mode = True

# class TileSchema(TileCreate):  # Inheriting TileCreate for read operations
#     id: int  # Assuming your model has an 'id' field

#     class Config:
#         orm_mode = True


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base  # Import your base class from your database setup
from pydantic import BaseModel
from typing import List

# SQLAlchemy Model
class Tile(Base):
    __tablename__ = 'tiles'
    __table_args__ = {'extend_existing': True}  # Allow redefinition of the table

    id: int = Column(Integer, primary_key=True, nullable=False)
    geom: str = Column(String, nullable=False)
    properties: dict = Column(String)  # Assuming properties are stored as JSON or String

# Pydantic Model (TileCreate)
class TileCreate(BaseModel):
    geom: str
    properties: dict

    class Config:
        orm_mode = True


# Pydantic Model (TileCreate)
class TileUpdate(BaseModel):
    geom: str
    properties: dict

    class Config:
        orm_mode = True

# SQLAlchemy Model Inheriting Pydantic Model (Tile)
class TileOut(TileCreate):
    id: int

    class Config:
        orm_mode = True
