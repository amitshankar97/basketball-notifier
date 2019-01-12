from pymongo import MongoClient
import os

client = MongoClient(os.environ['BASKETBALL_DB'])
db = client['basketball']

class DB:
    def __init__(self):
        self.games = db['close-game-tracker']

    def find_game(self, gameId):
        return self.games.find_one({'gameId': gameId})

    def insert_game(self, gameId):
        return self.games.insert_one({'gameId': gameId, 'sentNotification': True})