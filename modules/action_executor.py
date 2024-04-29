import webbrowser
from newsapi import NewsApiClient
from api_key import key
import os
from modules.database import Database

class ActionExecutor:
    def __init__(self, db):
        self.news_api = NewsApiClient(api_key=key)
        self.db = Database()

    def execute_action(self, action, target):
        if (action, target) == ('OPEN', 'GOOGLE'):
            webbrowser.open('https://www.google.com')
            return "Opening Google website..."
        elif (action, target) == ('OPEN', 'GMAIL'):
            webbrowser.open('https://mail.google.com')
            return "Opening Gmail website..."
        elif (action, target) == ('OPEN', 'YOUTUBE'):
            webbrowser.open('https://www.youtube.com')
            return "Opening YouTube website..."
        elif (action, target) == ('OPEN', 'LINKEDIN'):
            webbrowser.open('https://www.linkedin.com')
            return "Opening LinkedIn website..."
        elif (action, target) == ('OPEN', 'SCHOLAR'):
            webbrowser.open('https://scholar.google.com')
            return "Searching Scholar..."
        elif (action, target) == ('PLAY', 'MUSIC'):
            return "Playing music..."
        elif (action, target) == ('PLAY', 'MOVIES'):
            return "Playing movies..."
        elif (action, target) == ('CREATE', 'FOLDER'):
            folder_name = input("Enter folder name: ")
            os.mkdir(folder_name)
            return f"Created folder '{folder_name}'"
        elif (action, target) == ('GET', 'NEWS'):
            top_business_stories = self.news_api.get_top_headlines(category='business', language='en', country='us', page_size=5)
            stories_list = [f"{i + 1}. {article['title']}" for i, article in enumerate(top_business_stories['articles'])]
            interpretation = "Fetching the latest business news...\n"
            news_text = "\n".join(stories_list)
            return interpretation + news_text
        elif (action, target) in [('ADD', 'BOOK'), ('GET', 'BOOKS'), ('UPDATE', 'BOOK'), ('DELETE', 'BOOK')]:
            return self.db.execute_book(action, target)
        elif (action, target) in [('ADD', 'RECIPE'), ('GET', 'RECIPE'), ('UPDATE', 'RECIPE'), ('DELETE', 'RECIPE')]:
            return self.db.execute_recipe(action, target)
        elif (action, target) in [('ADD', 'TASK'), ('GET', 'TASK'), ('UPDATE', 'TASK'), ('DELETE', 'TASK')]:
            return self.db.execute_task(action, target)
        elif (action, target) in [('ADD', 'NOTE'), ('GET', 'NOTES'), ('UPDATE', 'NOTE'), ('DELETE', 'NOTES')]:
            return self.db.execute_note(action, target)
        elif (action, target) in [('ADD', 'MOVIE'), ('GET', 'MOVIE'), ('UPDATE', 'MOVIE'), ('DELETE', 'MOVIE')]:
            return self.db.execute_movie(action, target)
        elif (action, target) in [('ADD', 'SONG'), ('GET', 'SONG'), ('UPDATE', 'SONG'), ('DELETE', 'SONG')]:
            return self.db.execute_song(action, target)
        elif (action, target) in [('ADD', 'CONTACT'), ('GET', 'CONTACT'), ('UPDATE', 'CONTACT'), ('DELETE', 'CONTACT')]:
            return self.db.execute_contact(action, target)
        elif (action, target) in [('ADD', 'QUOTE'), ('GET', 'QUOTES'), ('UPDATE', 'QUOTE'), ('DELETE', 'QUOTE')]:
            return self.db.execute_quote(action, target)
        else:
            return "Action not supported."
