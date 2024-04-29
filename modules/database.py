import sqlite3

class Database:
    def __init__(self, db_file='data\\brain.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
    #Crud Functionality for Books
    def add_book(self):
        # Prompt the user to input book details
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year: ")
        summary = input("Enter a summary of the book: ")

        # Insert the book into the Books table
        insert_query = '''
            INSERT INTO Books (title, author, year, summary)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(insert_query, (title, author, year, summary))
        self.conn.commit()

        return "Book added successfully."

    def get_books(self):
        # Retrieve all books from the Books table
        select_query = '''
            SELECT * FROM Books
        '''
        self.cursor.execute(select_query)
        books = self.cursor.fetchall()

        if not books:
            return "No books found in the database."
        else:
            return books

    def update_book(self):
        # Prompt the user to input book title for updating
        title_to_update = input("Enter the title of the book to update: ")
        
        # Check if the book exists
        select_query = '''
            SELECT * FROM Books WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        book = self.cursor.fetchone()

        if not book:
            return f"Book with title '{title_to_update}' not found."

        # Prompt the user to input updated book details
        new_title = input("Enter the updated title of the book: ")
        author = input("Enter the updated author of the book: ")
        year = input("Enter the updated publication year: ")
        summary = input("Enter the updated summary of the book: ")

        # Update the specified book in the Books table based on the title
        update_query = '''
            UPDATE Books
            SET title = ?, author = ?, year = ?, summary = ?
            WHERE title = ?
        '''
        self.cursor.execute(update_query, (new_title, author, year, summary, title_to_update))
        self.conn.commit()

        return "Book updated successfully."

    def delete_book(self):
        # Prompt the user to input book title for deletion
        title_to_delete = input("Enter the title of the book to delete: ")

        # Check if the book exists
        select_query = '''
            SELECT * FROM Books WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        book = self.cursor.fetchone()

        if not book:
            return f"Book with title '{title_to_delete}' not found."

        # Delete the specified book from the Books table based on the title
        delete_query = '''
            DELETE FROM Books
            WHERE title = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Book deleted successfully."
    
        #Crud Functionality for Recipe
    def add_recipe(self):
        # Prompt the user to input recipe details
        title = input("Enter the title of the recipe: ")
        ingredients = input("Enter the ingredients: ")
        instructions = input("Enter the instructions: ")

        # Insert the recipe into the Recipes table
        insert_query = '''
            INSERT INTO Recipes (title, ingredients, instructions)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, (title, ingredients, instructions))
        self.conn.commit()

        return "Recipe added successfully."

    def get_recipe(self):
        # Retrieve all recipes from the Recipes table
        select_query = '''
            SELECT * FROM Recipes
        '''
        self.cursor.execute(select_query)
        recipes = self.cursor.fetchall()

        if not recipes:
            return "No recipes found in the database."
        else:
            return recipes

    def update_recipe(self):
        # Prompt the user to input recipe title for updating
        title_to_update = input("Enter the title of the recipe to update: ")
        
        # Check if the recipe exists
        select_query = '''
            SELECT * FROM Recipes WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        recipe = self.cursor.fetchone()

        if not recipe:
            return f"Recipe with title '{title_to_update}' not found."

        # Prompt the user to input updated recipe details
        new_title = input("Enter the title of the recipe: ")
        ingredients = input("Enter the ingredients: ")
        instructions = input("Enter the instructions: ")

        # Update the specified recipe in the Recipes table based on the title
        update_query = '''
            UPDATE Recipes
            SET title = ?, ingredients = ?, instructions = ?
            WHERE title = ?
        '''
        self.cursor.execute(update_query, (new_title, ingredients, instructions, title_to_update))
        self.conn.commit()

        return "Recipe updated successfully."

    def delete_recipe(self):
        # Prompt the user to input recipe title for deletion
        title_to_delete = input("Enter the title of the recipe to delete: ")

        # Check if the recipe exists
        select_query = '''
            SELECT * FROM Recipes WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        recipe = self.cursor.fetchone()

        if not recipe:
            return f"Recipe with title '{title_to_delete}' not found."

        # Delete the specified recipe from the Recipes table based on the title
        delete_query = '''
            DELETE FROM Recipes
            WHERE title = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Recipe deleted successfully."
    

    #Crud Functionality for To Do List
    def add_task(self):
        # Prompt the user to input recipe details
        task_description = input("Enter the task: ")
        due_date = input("Enter the due_date(dd/mm/yyyy): ")
        priority = input("Enter the priority number: ")

        # Insert the task into the ToDoList table
        insert_query = '''
            INSERT INTO ToDoList (task_description, due_date, priority)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, (task_description, due_date, priority))
        self.conn.commit()

        return "Task added successfully."

    def get_tasks(self):
        # Retrieve all tasks from the ToDoList table
        select_query = '''
            SELECT * FROM ToDoList
        '''
        self.cursor.execute(select_query)
        tasks = self.cursor.fetchall()

        if not tasks:
            return "No tasks found in the database."
        else:
            return tasks

    def update_task(self):
        # Prompt the user to input task title for updating
        title_to_update = input("Enter the title of the task to update: ")
        
        # Check if the task exists
        select_query = '''
            SELECT * FROM ToDoList WHERE task_description = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        task = self.cursor.fetchone()

        if not task:
            return f"Task with title '{title_to_update}' not found."

        # Prompt the user to input updated task details
        task_description = input("Enter the task: ")
        due_date = input("Enter the due_date(dd/mm/yyyy): ")
        priority = input("Enter the priority number: ")

        # Update the specified recipe in the Recipes table based on the title
        update_query = '''
            UPDATE ToDoList
            SET task_description = ?, due_date = ?, priority = ?
            WHERE task_description = ?
        '''
        self.cursor.execute(update_query, (task_description, due_date, priority, title_to_update))
        self.conn.commit()

        return "Task updated successfully."

    def delete_task(self):
        # Prompt the user to input task title for deletion
        title_to_delete = input("Enter the task to delete: ")

        # Check if the task exists
        select_query = '''
            SELECT * FROM ToDoList WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        task = self.cursor.fetchone()

        if not task:
            return f"Task with title '{title_to_delete}' not found."

        # Delete the specified task from the ToDoList table based on the title
        delete_query = '''
            DELETE FROM ToDoList
            WHERE task_description = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Task deleted successfully."

    #Crud Functionality for Notes
    def add_note(self):
        # Prompt the user to input recipe details
        title = input("Enter the Note title: ")
        content = input("Enter the Note content: ")
        category = input("Enter the instructions: ")

        # Insert the task into the Notes table
        insert_query = '''
            INSERT INTO Notes (title, content, category)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, (title, content, category))
        self.conn.commit()

        return "Note added successfully."

    def get_notes(self):
        # Retrieve all notes from the Notes table
        select_query = '''
            SELECT * FROM Notes
        '''
        self.cursor.execute(select_query)
        tasks = self.cursor.fetchall()

        if not tasks:
            return "No Notes found in the database."
        else:
            return tasks

    def update_note(self):
        # Prompt the user to input note title for updating
        title_to_update = input("Enter the title of the Note to update: ")
        
        # Check if the task exists
        select_query = '''
            SELECT * FROM Notes WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        task = self.cursor.fetchone()

        if not task:
            return f"Task with title '{title_to_update}' not found."

        # Prompt the user to input updated task details
        title = input("Enter the Note title: ")
        content = input("Enter the Note content: ")
        category = input("Enter the instructions: ")

        # Update the specified recipe in the Recipes table based on the title
        update_query = '''
            UPDATE Notes
            SET title = ?, content = ?, category = ?
            WHERE title = ?
        '''
        self.cursor.execute(update_query, (title, content, category, title_to_update))
        self.conn.commit()

        return "Note updated successfully."

    def delete_note(self):
        # Prompt the user to input Notes title for deletion
        title_to_delete = input("Enter the Notes to delete: ")

        # Check if the note exists
        select_query = '''
            SELECT * FROM Notes WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        note = self.cursor.fetchone()

        if not note:
            return f"Notes with title '{title_to_delete}' not found."

        # Delete the specified note from the Notes table based on the title
        delete_query = '''
            DELETE FROM Notes
            WHERE title = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Notes deleted successfully."

    #Crud Functionality for Movies
    def add_movie(self):
        # Prompt the user to input movie details
        title = input("Enter the movie title: ")
        director = input("Enter the director: ")
        release_year = input("Enter the release_year: ")
        genre = input("Enter the genre: ")
        summary = input("Enter the summary: ")

        # Insert the task into the Movies table
        insert_query = '''
            INSERT INTO Movies (title, director, release_year, genre, summary)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(insert_query, (title, director, release_year, genre, summary))
        self.conn.commit()

        return "Movie added successfully."

    def get_movies(self):
        # Retrieve all movies from the Movies table
        select_query = '''
            SELECT * FROM Movies
        '''
        self.cursor.execute(select_query)
        movies = self.cursor.fetchall()

        if not movies:
            return "No movies found in the database."
        else:
            return movies

    def update_movie(self):
        # Prompt the user to input note title for updating
        title_to_update = input("Enter the title of the Movie to update: ")
        
        # Check if the task exists
        select_query = '''
            SELECT * FROM Notes WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        movie = self.cursor.fetchone()

        if not movie:
            return f"Movie with title '{title_to_update}' not found."

        # Prompt the user to input updated movie details
        title = input("Enter the movie title: ")
        director = input("Enter the director: ")
        release_year = input("Enter the release_year: ")
        genre = input("Enter the genre: ")
        summary = input("Enter the summary: ")

        # Update the specified recipe in the Recipes table based on the title
        update_query = '''
            UPDATE Notes
            SET title = ?, director = ?, release_year = ?, genre = ?, summary = ?
            WHERE title = ?
        '''
        self.cursor.execute(update_query, (title, director, release_year, genre, summary, title_to_update))
        self.conn.commit()

        return "Movie updated successfully."

    def delete_movie(self):
        # Prompt the user to input Movie title for deletion
        title_to_delete = input("Enter the Movie to delete: ")

        # Check if the movie exists
        select_query = '''
            SELECT * FROM Movies WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        movie = self.cursor.fetchone()

        if not movie:
            return f"Notes with title '{title_to_delete}' not found."

        # Delete the specified movie from the Movies table based on the title
        delete_query = '''
            DELETE FROM Movies
            WHERE title = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Movie deleted successfully."

    #Crud Functionality for Music
    def add_music(self):
        # Prompt the user to input song details
        title = input("Enter the song title: ")
        artist = input("Enter the artist: ")
        album = input("Enter the album: ")
        year = input("Enter the year: ")
        genre = input("Enter the genre: ")

        # Insert the song into the Music table
        insert_query = '''
            INSERT INTO Music (title, artist, album, year, genre)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(insert_query, (title,  artist, album, year, genre))
        self.conn.commit()

        return "Song added successfully."

    def get_music(self):
        # Retrieve all music from the Music table
        select_query = '''
            SELECT * FROM Music
        '''
        self.cursor.execute(select_query)
        music = self.cursor.fetchall()

        if not music:
            return "No movies found in the database."
        else:
            return music

    def update_music(self):
        # Prompt the user to input song title for updating
        title_to_update = input("Enter the title of the song to update: ")
        
        # Check if the song exists
        select_query = '''
            SELECT * FROM Music WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        song = self.cursor.fetchone()

        if song:
            return f"Song with title '{title_to_update}' not found."

        # Prompt the user to input updated song details
        title = input("Enter the song title: ")
        artist = input("Enter the artist: ")
        album = input("Enter the album: ")
        year = input("Enter the year: ")
        genre = input("Enter the genre: ")

        # Update the specified song in the Music table based on the title
        update_query = '''
            UPDATE Music
            SET title = ?, artist = ?, album = ?, year = ?, genre = ?
            WHERE title = ?
        '''
        self.cursor.execute(update_query, (title,  artist, album, year, genre, title_to_update))
        self.conn.commit()

        return "Song updated successfully."

    def delete_music(self):
        # Prompt the user to input Song title for deletion
        title_to_delete = input("Enter the Song to delete: ")

        # Check if the movie exists
        select_query = '''
            SELECT * FROM Music WHERE title = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        song = self.cursor.fetchone()

        if not song:
            return f"Song with title '{title_to_delete}' not found."

        # Delete the specified movie from the Movies table based on the title
        delete_query = '''
            DELETE FROM Music
            WHERE title = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Song deleted successfully."

    #Crud Functionality for Contacts
    def add_contact(self):
        # Prompt the user to input Contact details
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")

        # Insert the contact into the Contacts table
        insert_query = '''
            INSERT INTO Contacts (name, phone_number, email)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, (name, phone_number, email))
        self.conn.commit()

        return "Contact added successfully."

    def get_contacts(self):
        # Retrieve all contacts from the Contacts table
        select_query = '''
            SELECT * FROM Contacts
        '''
        self.cursor.execute(select_query)
        contacts = self.cursor.fetchall()

        if not contacts:
            return "No contacts found in the database."
        else:
            return contacts

    def update_contact(self):
        # Prompt the user to input contact title for updating
        title_to_update = input("Enter the title of the contact to update: ")
        
        # Check if the song exists
        select_query = '''
            SELECT * FROM Contacts WHERE name = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        contact = self.cursor.fetchone()

        if contact:
            return f"Song with title '{title_to_update}' not found."

        # Prompt the user to input updated contact details
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")

        # Update the specified contact in the Contacts table based on the title
        update_query = '''
            UPDATE Contacts
            SET name = ?, phone_number = ?, email = ?
            WHERE name = ?
        '''
        self.cursor.execute(update_query, (name, phone_number, email, title_to_update))
        self.conn.commit()

        return "Contact updated successfully."

    def delete_contact(self):
        # Prompt the user to input contact title for deletion
        title_to_delete = input("Enter the contact to delete: ")

        # Check if the contact exists
        select_query = '''
            SELECT * FROM Contacts WHERE name = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        contact = self.cursor.fetchone()

        if not contact:
            return f"Contact with title '{title_to_delete}' not found."

        # Delete the specified contact from the Contacts table based on the title
        delete_query = '''
            DELETE FROM Contacts
            WHERE name = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Contact deleted successfully."
    
    #Crud Functionality for Quotes
    def add_quote(self):
        # Prompt the user to input Quote details
        quote = input("Enter the quote: ")
        author = input("Enter the author: ")

        # Insert the quote into the Quotes table
        insert_query = '''
            INSERT INTO Quotes (quote, author)
            VALUES (?, ?)
        '''
        self.cursor.execute(insert_query, (quote, author))
        self.conn.commit()

        return "Quote added successfully."

    def get_quotes(self):
        # Retrieve all quotes from the Quotes table
        select_query = '''
            SELECT * FROM Quotes
        '''
        self.cursor.execute(select_query)
        quotes = self.cursor.fetchall()

        if not quotes:
            return "No Quotes found in the database."
        else:
            return quotes

    def update_quote(self):
        # Prompt the user to input quote for updating
        title_to_update = input("Enter the quote to update: ")
        
        # Check if the song exists
        select_query = '''
            SELECT * FROM Quotes WHERE quote = ?
        '''
        self.cursor.execute(select_query, (title_to_update,))
        quote = self.cursor.fetchone()

        if quote:
            return f"Quote with info '{title_to_update}' not found."

        # Prompt the user to input updated quote details
        quote = input("Enter the quote: ")
        author = input("Enter the author: ")

        # Update the specified quote in the Quotes table based on the title
        update_query = '''
            UPDATE Quotes
            SET quote = ?, author = ?
            WHERE quote = ?
        '''
        self.cursor.execute(update_query, (quote, author, title_to_update))
        self.conn.commit()

        return "Quotes updated successfully."

    def delete_quote(self):
        # Prompt the user to input quote for deletion
        title_to_delete = input("Enter the quote to delete: ")

        # Check if the contact exists
        select_query = '''
            SELECT * FROM Quotes WHERE quote = ?
        '''
        self.cursor.execute(select_query, (title_to_delete,))
        contact = self.cursor.fetchone()

        if not contact:
            return f"Contact with title '{title_to_delete}' not found."

        # Delete the specified contact from the Contacts table based on the title
        delete_query = '''
            DELETE FROM Contacts
            WHERE quote = ?
        '''
        self.cursor.execute(delete_query, (title_to_delete,))
        self.conn.commit()

        return "Contact deleted successfully."

    def close_connection(self):
        self.conn.close()




