import requests
import os
from db import DB

MAKER_URL = os.environ['MAKER_URL']
NBA_BASE = 'https://data.nba.net/10s'

INTERESTING_TEAMS = ['LAL', 'BOS', 'DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'MEM', 'MIL', 'OKC', 'PHI', 'POR', 'TOR', 'UTA']

def sendNotification(team1, team2, time):
    payload = {team1, team2, score}
    r = requests.post(MAKER_URL, data=payload)

def NBATodayScoreboard():
    r = requests.get(NBA_BASE + '/prod/v2/today.json').json()
    todayScoreboard = r['links']['todayScoreboard']
    return requests.get(NBA_BASE + todayScoreboard).json()

if __name__ == '__main__':
    scoreboard = NBATodayScoreboard()
    games = scoreboard['games']

    for game in games:

        if game['vTeam']['triCode'] in INTERESTING_TEAMS or game['hTeam']['triCode'] in INTERESTING_TEAMS:

            if game['isGameActivated'] and game['period']['current'] >= 4:

                clock = game['clock'].split(':')

                if len(clock) < 2:
                    continue


                minutes = int(clock[0])

                pts_difference = abs(int(game['hTeam']['score']) - int(game['vTeam']['score']))

                current_period = game['period']['current']
                period = ""
                if current_period > 4:
                    period = (str(current_period % 4) + ' OT')
                else:
                    period = str(current_period) + ' Q'

                if minutes <= 6 and  pts_difference < 10:
                    # mongo = DB()
                    # db_game = mongo.find_game(game['gameId'])
                    # print(db_game)

                    time_left = period + game['clock']

                    sendNotification(game['hTeam'], game['vTeam'], time_left)