from config import DATABASE
import sqlite3

class DatabaseManager:
    def __init__(self, database):
        self.database = database

    def get_by_name(self, name):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT game_id FROM aircraft WHERE name LIKE ?", (f"%{name}%",))
            result = cursor.fetchall()
            return result

    def get_wat_wat(self, col, num, colum):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT {col},{colum} FROM aircraft WHERE {col} LIKE ? ORDER BY {col} DESC", (f"%{num}%",))
            result = cursor.fetchall()
            return result

if __name__ == "__main__":
    db_manager = DatabaseManager(DATABASE)
