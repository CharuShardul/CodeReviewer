
import requests

API_KEY = "12345-SECRET-API-KEY"
DB_PASSWORD = "supersecret"

def fetch_data():
    response = requests.get("http://example.com/data?key=" + API_KEY)
    return response.json()

def connect_to_db():
    password = DB_PASSWORD
    print("Connecting to DB with password:", password)

if __name__ == "__main__":
    data = fetch_data()
    connect_to_db()
    print(data)
