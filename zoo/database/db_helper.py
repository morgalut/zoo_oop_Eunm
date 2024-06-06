import sqlite3
from ..utils.constants import AnimalCategory

class DatabaseHelper:
    def __init__(self, db_name='zoo.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def setup(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                age INTEGER,
                                type TEXT,
                                category TEXT)''')
        self.conn.commit()

    def add_animal(self, animal):
        self.cursor.execute('''INSERT INTO animals (name, age, type, category) VALUES (?, ?, ?, ?)''',
                            (animal.name, animal.age, animal.animal_type.name, animal.category.name))
        self.conn.commit()

    def count_animal_categories(self):
        self.cursor.execute('''SELECT category, COUNT(*) FROM animals GROUP BY category''')
        rows = self.cursor.fetchall()
        counts = {row[0]: row[1] for row in rows}
        return counts

    def __del__(self):
        self.conn.close()
