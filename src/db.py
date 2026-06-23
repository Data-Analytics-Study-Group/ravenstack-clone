import psycopg
from src.config import DATABASE_URL

def get_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in config")

    return psycopg.connect(DATABASE_URL)