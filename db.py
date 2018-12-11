from pymongo import MongoClient
import os

client = MongoClient(os.environ['DB_CONN_STRING'])
db = client['close-game-tracker']

class DB:
    def __init__(self):
        self.games = db['games']

    def find_game(self, gameId):
        return self.games.find_one({'gameId': gameId})

    def insert_game(self, gameId):
        return self.games.insert_one({'gameId': gameId, 'sentNotification': False})

    def update_game(self, gameId):
        new_game = {
            'gameId': gameId,
            'sentNotification': False
        }

        return self.games.update_one({'gameId': gameId}, {"$set": new_game})