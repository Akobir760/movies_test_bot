
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_CONFIG = {
    "database": DB_NAME,
    "user": DB_USER,
    "port": DB_PORT,
    "host": DB_HOST,
    "password": DB_PASS
}
def get_connection():


    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.Error as e:
        print(e)



CHANNELS = [
    {
        "name": "channel 1", 
        "link": "test_channeln66",
        "chat_id": 2799858045
    }
]

TOKEN = os.getenv("token")
ADMIN_ID = 844817222 