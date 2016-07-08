#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, operator
from kickerrankade import Kickertool

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print "Usage: %s filename" % sys.argv[0]
        sys.exit(0)
        
    kicker = Kickertool(file)

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
