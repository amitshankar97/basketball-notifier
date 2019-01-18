from pymongo import MongoClient
import os
from datetime import datetime

client = MongoClient(os.environ['BASKETBALL_DB'])
db = client['basketball']

class DB:
    def __init__(self):
        self.db = db
        self.games = db['close-game-tracker']
        self.log = db['scrape-log']

    def find_game(self, gameId):
        return self.games.find_one({'gameId': gameId})

    def insert_game(self, gameId):
        return self.games.insert_one({'gameId': gameId, 'sentNotification': True})

    def logToMongo(self):
        self.log.insert_one({'time' : datetime.utcnow()})

    def logException(self, e):
        self.log.insert_one({'exception': e})