import pytest
from fastapi.testclient import TestClient
# from app.main import app  # Import your FastAPI app
import sys
import os

# Add the app directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import app  # Now you can import the app


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Geospatial Pipeline API!"}

def test_create_tile():
    # Test data
    tile_data = {
        "geom": "POINT(1 1)",
        "properties": {"name": "Tile 1"}
    }
    response = client.post("/tiles/", json=tile_data)  # Assuming a POST route to create a tile
    assert response.status_code == 201
    assert response.json()["geom"] == "POINT(1 1)"
    assert response.json()["properties"]["name"] == "Tile 1"

def test_get_tile():
    # Test getting a tile
    response = client.get("/tiles/1")  # Assuming route to fetch a tile by ID
    assert response.status_code == 200
    assert "geom" in response.json()

def test_pipeline():
    # Test the ingestion pipeline (adjust based on your route)
    response = client.post("/pipeline/ingest", json={})
    assert response.status_code == 200
    assert "status" in response.json()
