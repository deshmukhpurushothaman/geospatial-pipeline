import json
import os
import requests
from .models import Tile
from .database import SessionLocal
from sqlalchemy import text

def fetch_geojson_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def ingest_data():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        geojson_path = os.path.join(script_dir, "../doc/karnataka.geojson")

        if not os.path.exists(geojson_path):
            raise FileNotFoundError(f"GeoJSON file not found at {geojson_path}")

        print(f"Resolved geojson path: {geojson_path}")
        geojson_data = fetch_geojson_data(geojson_path)
        db = SessionLocal()

        for feature in geojson_data['features']:
            geom = feature['geometry']
            properties = feature['properties']

            # Convert the 'geom' to a geometry type using ST_GeomFromGeoJSON and add it to the database
            geom_str = json.dumps(geom)  # Keep GeoJSON as string for now

            # Create SQL query to insert the geometry into the database
            sql = text("""
                INSERT INTO tiles (geom, properties)
                VALUES (ST_GeomFromGeoJSON(:geom), :properties)
            """)
            db.execute(sql, {'geom': geom_str, 'properties': json.dumps(properties)})

        db.commit()
        db.close()
        print("Data successfully ingested into the database!")
    except Exception as e:
        print(f"Error occurred: {e}")
