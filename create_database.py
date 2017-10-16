import sqlite3
import os

def create_database():
    """ Creates database if it does not exist """
    if not os.path.exists('database.db'):
        os.path.join(os.path.dirname(__file__), "database.db")
        print('Database created successfully.')
    else:
        print('Database already exists.')


def create_table():
    """ Creates table in database """
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    query = ("""CREATE TABLE IF NOT EXISTS 'todos'(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            done INTEGER NOT NULL)""")

    cursor.execute(query)
    connection.commit()
    connection.close()


def main():
    create_database()
    create_table()

if __name__ == '__main__':
    main()
