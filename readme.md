# Einstein AI Assistant

Einstein is an AI assistant built in Python that can perform various tasks based on user commands. It uses natural language processing (NLP) for interpreting input and executing actions accordingly.

## Features

- **Natural Language Understanding (NLU)**: Parses user input to extract actions and targets using part-of-speech tagging.
- **Action Execution**: Executes corresponding actions based on parsed commands, such as opening websites, playing music, managing tasks, and more.
- **Database Interaction**: Supports CRUD (Create, Read, Update, Delete) operations for managing books, recipes, tasks, notes, movies, music, contacts, and quotes in a SQLite database.
- **Modular Architecture**: Organized into separate modules (`language`, `action_executor`, and `database`) for better code structure and maintainability.
  
## Usage

1. **Setup**:
   - Ensure Python 3.x is installed on your system.
   - Install required libraries using `pip`:
     ```bash
     pip install nltk newsapi-python sqlite3
     ```

2. **Configuration**:
   - Obtain a News API key from [NewsAPI](https://newsapi.org/) and update `api_key.py` with your key.
   - Customize the `dictionary` in `list.py` to define supported commands.

3. **Execution**:
   - Run `main.py` to start the Einstein AI assistant.
   - Enter commands in natural language (e.g., "Open Google", "Add a book").

4. **Supported Actions**:
   - **Open**: Open specific websites (e.g., Google, YouTube).
   - **Play**: Play music or movies.
   - **Create**: Create folders.
   - **Get**: Fetch news headlines, books, recipes, tasks, notes, movies, music, contacts, or quotes.
   - **Add**: Add new entries to the database (e.g., books, recipes, tasks).
   - **Update**: Update existing entries in the database (e.g., update a book).
   - **Delete**: Delete entries from the database (e.g., delete a task).

## File Structure

- `brain.py`: Entry point for the Einstein AI assistant.
- `language.py`: Module for natural language processing and interpretation.
- `action_executor.py`: Module for executing actions based on interpreted commands.
- `database.py`: Module for interacting with the SQLite database.
- `api_key.py`: Stores API keys (e.g., NewsAPI key).
- `list.py`: Defines the dictionary mapping commands to actions.
- `data/brain.db`: SQLite database file for storing persistent data.

## Contributions

Contributions to improve the functionality and code quality of this project are welcome! If you have any suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
