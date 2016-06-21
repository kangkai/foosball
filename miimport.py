#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys, time, re, json, operator

kickername_rankadename_mapping = {
    u"康凯":u"尹康凯",
    u"尹康凯":u"尹康凯",
    u"孟晓然":u"*Meng Xiaoran",
    u"赵瑞华":u"Zhaoruihua",
    u"曹聃":u"曹先森",
    u"曹凯":u"*Cao Kai",
    u"慧芳":u"*Liu Huifang",
    u"施磊":u"*Shi Lei",
    u"任恬":u"*Ren Tian",
    u"苏本昌":u"苏本昌",
    u"本昌":u"苏本昌",
    u"肖晓林":u"*Xiao Xiaolin",
    u"国祝":u"*guozhu",
    u"张小武":u"XiaowuZhang",
    u"韩广义":u"HanGuangyi",
    u"广义":u"HanGuangyi",
    u"Matt":u"*matt",
    u"张茜明":u"zhangximing",
    u"茜明":u"zhangximing",
    u"博士":u"*boshi",
    u"鑫岩":u"Xinyan Xing",
    u"邢鑫岩":u"Xinyan Xing",
    u"Lisa":u"*Lisa",
    u"lisa":u"*Lisa",
    u"关剑喜（替补）":u"*guanjianxi",
    u"彭亚":u"*Peng Ya",
    u"教练":u"*Gu Yafei",
    u"佐罗":u"*Zuo Luo"
}

class Kickertool(object):
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

        # parse players
        self.players = {}
        for p in parsed_json['players']:
            self.players[p['id']] = p['name']

        # parse plays
        self.plays = {}
        for p in parsed_json['plays']:
            if not p['deactivated']:
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
            self.teams[t['id']] = [t['players'][0]['id'], t['players'][1]['id']]
        

    def num_players(self):
        """Return number of players in json file"""
        return len(self.players)

    def num_teams(self):
        return len(self.teams)

    def num_plays(self):
        return len(self.plays)

class Rankade(object):
    def __init__(self, username, passwd):
        self.driver = webdriver.Chrome()
        driver = self.driver

        driver.implicitly_wait(300) # seconds
        driver.get('https://rankade.com/')
        assert 'rankade' in driver.title

        driver.find_element_by_css_selector("a.sign-button.sign-in-button").click()
        assert 'Sign in' in driver.title

        input = driver.find_element_by_name("email")
        input.send_keys(username)
        input = driver.find_element_by_name("password")
        input.send_keys(passwd)
        driver.find_element_by_name("submit").click()
        assert 'rankade' in driver.title
        driver.find_element_by_id("dashboardLink").click()
        # assert 'rankade - My dashboard' in driver.title
        driver.find_element_by_link_text("mifoosball").click()
        # driver.save_screenshot('mifoosball.png')
        # assert 'mifoosball' in driver.title

    def insert_one_match(self, match):
        # match is a list, e.g.: [u'孟晓然', u'苏本昌', 5, u'Lisa', u'慧芳', 2] """
        driver = self.driver

        #WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        #                                                    'a.pull-right.btn.btn-default.btn-small.newMatchButton')))
        time.sleep(10) # FIXME: above wait seems not work very well
        driver.find_element_by_css_selector("a.pull-right.btn.btn-default.btn-small.newMatchButton").click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-default.btn-sm.next.pull-right')))
        driver.execute_script("matchForm.toggleAdditionalOptions();")

        select = Select(driver.find_element_by_name('countFactions'))
        select.select_by_index(0)
        driver.find_element_by_name('newGameMatch').send_keys("Foosball")
        driver.find_element_by_name('newPlaceMatch').send_keys("Xiaomi Wuchaicheng 11F")
        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        xpath = '//label[text()=' + '" ' + match[0] + '"]'
        driver.find_element_by_xpath(xpath).click()
        xpath = '//label[text()=' + '" ' + match[1] + '"]'
        driver.find_element_by_xpath(xpath).click()

        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        xpath = '//div[@data-step-id="1"]/div/div/p/label[text()=' + '" ' + match[3] + '"]'
        driver.find_element_by_xpath(xpath).click()
        xpath = '//div[@data-step-id="1"]/div/div/p/label[text()=' + '" ' + match[4] + '"]'
        driver.find_element_by_xpath(xpath).click()

        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        score1 = match[2]
        score2 = match[5]

        driver.find_element_by_css_selector('input.form-control.input-xs').send_keys(score1)
        driver.find_element_by_xpath('//div[@data-faction-step-class="matchStep3"]/div[3]/input').send_keys(score2)

        driver.find_element_by_name('matchNotes').send_keys("Auto inputed by Yin Kangkai's bot")
        driver.find_element_by_css_selector('a.btn.btn-primary.additionalButton').click()

        print "done"
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Usage: %s xxx.ktool username passwd" % sys.argv[0]
        print "\t xxx.ktool: file exported from kickertool"
        print "\t username/passwd: your rankade user/pass"
        sys.exit(0)

    kicker = Kickertool(sys.argv[1])
    print "Number of plays: ", kicker.num_plays()

    rankade = Rankade(sys.argv[2], sys.argv[3])

    index = 1
    for p in kicker.plays.keys():
        print "%-3d:" % index,
        score1 = kicker.plays[p][0][1]
        score2 = kicker.plays[p][1][1]
        team1 = kicker.plays[p][0][0]
        team2 = kicker.plays[p][1][0]
        pid = kicker.teams[team1][0]
        t1_player1 = kicker.players[pid]
        pid = kicker.teams[team1][1]
        t1_player2 = kicker.players[pid]
        pid = kicker.teams[team2][0]
        t2_player1 = kicker.players[pid]
        pid = kicker.teams[team2][1]
        t2_player2 = kicker.players[pid]

        print "%s/%s(%d) \tvs\t %s/%s(%d)" % (t2_player1, t2_player2, score2,
                                              t1_player1, t1_player2, score1)
        one_match = [kickername_rankadename_mapping[t2_player1],
                     kickername_rankadename_mapping[t2_player2],
                     score2,
                     kickername_rankadename_mapping[t1_player1],
                     kickername_rankadename_mapping[t1_player2],
                     score1]
        rankade.insert_one_match(one_match)

        index = index + 1
