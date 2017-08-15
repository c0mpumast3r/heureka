# -*- coding: cp1252 -*-
# Author: Franklet Semilla
# Date: 8/14/2017

import requests

if __name__ == '__main__':
    nhl_stats = []
    r = requests.get('https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-02-07&endDate=2017-02-07')
    r.json()
    for i in range(len(r.json()['dates'][0]['games'])):
        game_dict = {}
        game_dict['venue'] = r.json()['dates'][0]['games'][i]['venue']['name']
        game_dict['team_home'] = {
                                    'name': r.json()['dates'][0]['games'][i]['teams']['home']['team']['name'],
                                    'wins': r.json()['dates'][0]['games'][i]['teams']['home']['leagueRecord']['wins'],
                                    'losses': r.json()['dates'][0]['games'][i]['teams']['home']['leagueRecord']['losses'],
                                    'ot': r.json()['dates'][0]['games'][i]['teams']['home']['leagueRecord']['ot']
                                    }
        game_dict['team_away'] = {
                                    'name': r.json()['dates'][0]['games'][i]['teams']['away']['team']['name'],
                                    'wins': r.json()['dates'][0]['games'][i]['teams']['away']['leagueRecord']['wins'],
                                    'losses': r.json()['dates'][0]['games'][i]['teams']['away']['leagueRecord']['losses'],
                                    'ot': r.json()['dates'][0]['games'][i]['teams']['away']['leagueRecord']['ot']
                                    }

        print "\n--------------------------"
        print "Venue: ", game_dict['venue']
        print "Home Team: ", game_dict['team_home']['name']
        print "    Wins: ", game_dict['team_home']['wins']
        print "    Losses: ", game_dict['team_home']['losses']
        print "    OT: ", game_dict['team_home']['ot']
        print "Away Team: ", game_dict['team_away']['name']
        print "    Wins: ", game_dict['team_home']['wins']
        print "    Losses: ", game_dict['team_home']['losses']
        print "    OT: ", game_dict['team_home']['ot']

        nhl_stats += [game_dict]

    print "\n\nFull Dict: \n"
    print nhl_stats
