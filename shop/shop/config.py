from os import getenv
from dotenv import load_dotenv

load_dotenv()


DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
SECRET_KEY = getenv("SECRET_KEY")