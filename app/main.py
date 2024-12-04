from fastapi import FastAPI
from .crud import create_tile, get_tile, update_tile, delete_tile
from .schemas import TileCreate, TileUpdate
from .pipeline import ingest_data

app = FastAPI()

# def __init__():
# ingest_data()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Geospatial Pipeline API!"}

@app.get("/tiles/{tile_id}")
def read_tile(tile_id: int):
    return get_tile(tile_id)

@app.post("/tiles/")
def create_new_tile(tile: TileCreate):
    return create_tile(tile)

@app.put("/tiles/{tile_id}")
def update_existing_tile(tile_id: int, tile: TileUpdate):
    return update_tile(tile_id, tile)

@app.delete("/tiles/{tile_id}")
def delete_existing_tile(tile_id: int):
    return delete_tile(tile_id)
