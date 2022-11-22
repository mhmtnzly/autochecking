"""A database encapsulating collections of data from data folder.
"""

import os
from dotenv import load_dotenv
import psycopg2 as db_connect

load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
host_name = 'localhost'
database_name = DB_NAME

connection = db_connect.connect(
    host=host_name, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

cursor = connection.cursor()

