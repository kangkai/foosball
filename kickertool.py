#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, operator

class KickertoolJson(object):
    """Handle json from kickertool output
    properties:
    players: dict for players {player1_id: name, ...}
    teams: dict for teams {team_id: [player1_id, player2_id], ...}
    plays: dict for plays {play_id: [(team1_id, score), (team2_id: score)], ...}
    """

    def __init__(self, path):
        """parse the file/path"""
        file = open(path)
        print "Load file name: ", file.name
        str = file.read()
        # print "string: ", str
        file.close()

        parsed_json = json.loads(str)
        print "id: %s" % parsed_json["id"]
        print "created: %s" % parsed_json["created"]
        self.date = parsed_json["created"].encode('ascii')[0:10]
        print "date: %s" % self.date

        # parse players
        self.players = {}
        for p in parsed_json['players']:
            self.players[p['id']] = p['name']

        # parse plays
        self.plays = {}
        for p in parsed_json['plays']:
            if p['valid']:
                scores = {}
                score1 = p['disciplines'][0]['sets'][0]['team1']
                score2 = p['disciplines'][0]['sets'][0]['team2']
                scores[p['team1']['id']] = score1
                scores[p['team2']['id']] = score2
                sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
                self.plays[p['id']] = sorted_scores

        # parse teams
        self.teams = {}
        for t in parsed_json['teams']:
            if len(t['players']) == 2:
                   self.teams[t['id']] = [t['players'][0]['id'], t['players'][1]['id']]
            else:
                   self.teams[t['id']] = [t['players'][0]['id']]
        

    def num_players(self):
        """Return number of players in json file"""
        return len(self.players)

    def num_teams(self):
        return len(self.teams)

    def num_plays(self):
        return len(self.plays)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print "Usage: %s filename" % sys.argv[0]
        sys.exit(0)
        
    kicker = KickertoolJson(file)

    print "Number of players: ", kicker.num_players()
    for i in kicker.players.keys():
        print i, ":", kicker.players[i].encode('utf8')

    """
    print "Number of plays: ", kicker.num_plays()
    for i in kicker.plays.keys():
        print i, ":"
        for j in kicker.plays[i].keys():
            print "  ",
            print j, kicker.plays[i][j]

    print "Number of teams: ", kicker.num_teams()
    """

    print "Number of plays: ", kicker.num_plays()
    #print "%s/%s(%s) : %s/%s(%s)" % ()
    index = 1
    for p in kicker.plays.keys():
        print "%-3d:" % index,
        score1 = kicker.plays[p][0][1]
        score2 = kicker.plays[p][1][1]
        team1 = kicker.plays[p][0][0]
        team2 = kicker.plays[p][1][0]
        pid = kicker.teams[team1][0]
        t1_player1 = kicker.players[pid]
        t1_player2 = ""
        if len(kicker.teams[team1]) == 2:
            pid = kicker.teams[team1][1]
            t1_player2 = kicker.players[pid]
        pid = kicker.teams[team2][0]
        t2_player1 = kicker.players[pid]
        t2_player2 = ""
        if len(kicker.teams[team2]) == 2:
            pid = kicker.teams[team2][1]
            t2_player2 = kicker.players[pid]

        print "%s/%s(%d) \tvs\t %s/%s(%d)" % (t2_player1.encode('utf8'),
                                              t2_player2.encode('utf8'),
                                              score2,
                                              t1_player1.encode('utf8'),
                                              t1_player2.encode('utf8'),
                                              score1)
        index = index + 1
