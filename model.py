import psycopg2
import json

class Database:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.connection.cursor()

    def get_maize_areas(self):
        # Query to fetch maize areas
        self.cursor.execute("SELECT name_2, ST_AsGeoJSON(geom) FROM matuga")
        maize_areas = self.cursor.fetchall()
        return maize_areas

    def close(self):
        self.cursor.close()
        self.connection.close()
