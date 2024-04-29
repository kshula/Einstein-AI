import sqlite3

# Function to create tables in the database
def create_tables():
    # Connect to the SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('data//brain.db')
    cursor = conn.cursor()

    # Create Books Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER,
            summary TEXT
        )
    ''')

    # Create Recipes Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            recipe_id INTEGER PRIMARY KEY,
            title TEXT,
            ingredients TEXT,
            instructions TEXT
        )
    ''')

    # Create ToDo List Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ToDoList (
            task_id INTEGER PRIMARY KEY,
            task_description TEXT,
            due_date DATE,
            priority INTEGER
        )
    ''')

    # Create Notes Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Notes (
            note_id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            category TEXT
        )
    ''')

    # Create Movies Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            movie_id INTEGER PRIMARY KEY,
            title TEXT,
            director TEXT,
            release_year INTEGER,
            genre TEXT,
            summary TEXT
        )
    ''')

    # Create Music Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Music (
            song_id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            album TEXT,
            year INTEGER,
            genre TEXT
        )
    ''')

    # Create Contacts Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contacts (
            contact_id INTEGER PRIMARY KEY,
            name TEXT,
            phone_number TEXT,
            email TEXT
        )
    ''')

    # Create Quotes Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Quotes (
            quote_id INTEGER PRIMARY KEY,
            quote TEXT,
            author TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Execute the function to create tables
if __name__ == '__main__':
    create_tables()
    print("Tables created successfully.")
