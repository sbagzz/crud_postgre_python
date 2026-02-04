from dotenv import load_dotenv
import psycopg2 as pg
import os

load_dotenv()

def conectar():
        return pg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )