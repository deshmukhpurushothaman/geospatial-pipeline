import json
from .models import Tile
from .database import SessionLocal
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func

def get_tile(tile_id: int):
    db: Session = SessionLocal()
    tile = db.query(Tile.id, func.ST_AsGeoJSON(Tile.geom).label('geom'), Tile.properties).filter(Tile.id == tile_id).first()

    if tile:
        # Now 'tile.geom' is a GeoJSON string, no need to load from JSON
        tile_geom = tile.geom  # This is now a valid GeoJSON string
        tile_properties = tile.properties
        return {"id": tile.id, "geom": tile_geom, "properties": tile_properties}
    return None

def create_tile(db: Session, tile_data: schemas.TileCreate):
    # Convert 'geom' to GeoJSON string before storing
    geom_str = json.dumps(tile_data.geom)  # Assuming geom is a dictionary

    db_tile = models.Tile(
        geom=geom_str,
        properties=tile_data.properties
    )
    db.add(db_tile)
    db.commit()
    db.refresh(db_tile)
    return db_tile

def update_tile(db: Session, tile_id: int, tile_data: schemas.TileUpdate):
    db_tile = db.query(models.Tile).filter(models.Tile.id == tile_id).first()
    if db_tile:
        # Convert updated 'geom' to GeoJSON string before updating
        geom_str = json.dumps(tile_data.geom)
        db_tile.geom = geom_str
        db_tile.properties = tile_data.properties
        db.commit()
        db.refresh(db_tile)
    return db_tile

def delete_tile(tile_id: int):
    db: Session = SessionLocal()
    db_tile = db.query(Tile).filter(Tile.id == tile_id).first()
    if db_tile:
        db.delete(db_tile)
        db.commit()
    return {"message": "Tile deleted successfully"}
