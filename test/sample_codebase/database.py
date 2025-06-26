
from config import DB_HOST, DB_PORT, USERNAME, PASSWORD

def connect():
    connection_string = f"postgresql://{USERNAME}:{PASSWORD}@{DB_HOST}:{DB_PORT}/mydb"
    print("Connecting to database with:", connection_string)
