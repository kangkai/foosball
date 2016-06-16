#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys, time, re
import json

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
        driver.save_screenshot('mifoosball.png')
        # assert 'mifoosball' in driver.title

    def insert_one_match(self, match):
        # match is a dict: {} """
        driver = self.driver

        driver.find_element_by_css_selector("a.pull-right.btn.btn-default.btn-small.newMatchButton").click()
        select = Select(driver.find_element_by_name('countFactions'))
        option = select.first_selected_option
        select.select_by_index(0)
        driver.find_element_by_name('newGameMatch').send_keys("Foosball")
        #driver.find_element_by_id('additionalOptionButton').click()
        #driver.find_element_by_css_selector('a.btn.btn-xs.btn-default').click()
        driver.find_element_by_name('newPlaceMatch').send_keys("Xiaomi Wuchaicheng 11F")
        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        xpath = '//label[text()=' + '" 尹康凯"' + ']'
        driver.find_element_by_xpath(xpath).click()
        xpath = '//label[text()=' + '" 曹先森"' + ']'
        driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        xpath = '//label[text()=' + '" Zhaoruihua"' + ']'
        driver.find_element_by_xpath(xpath).click()
        xpath = '//label[text()=' + '" Xinyan Xing"' + ']'
        driver.find_element_by_xpath(xpath).click()
        xpath = '//label[text()=' + '" 苏本昌"' + ']'
        driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_css_selector('button.btn.btn-default.btn-sm.next.pull-right').click()

        score1 = 5
        score2 = 3

        driver.find_element_by_css_selector('input.form-control.input-xs').send_keys(score1)
        driver.find_element_by_xpath('//div[@data-faction-step-class="matchStep3"]/div[3]/input').send_keys(score2)

    
    def test_rankade(self):
        driver = self.driver


        driver.find_element_by_name("newGameMatch").send_keys("Foosball")
        driver.find_element_by_css_selector("span.more").click()
        driver.find_element_by_xpath("//form[@id='newMatchForm']/div[5]/div/div[3]/button").click()
        driver.find_element_by_xpath("(//input[@name='f0_ids[]'])[12]").click()
        driver.find_element_by_xpath("//form[@id='newMatchForm']/div[5]/div/div[3]/button").click()
        driver.find_element_by_xpath("(//input[@name='f1_ids[]'])[15]").click()
        driver.find_element_by_xpath("//form[@id='newMatchForm']/div[5]/div/div[3]/button").click()
        driver.find_element_by_css_selector("div.col-xs-8.matchResultRowOptionSwitch > a > img").click()
        driver.find_element_by_css_selector("input.form-control.input-xs").clear()
        driver.find_element_by_css_selector("input.form-control.input-xs").send_keys("1")
        driver.find_element_by_xpath("(//input[@value=''])[6]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[6]").send_keys("1")
        driver.find_element_by_link_text("Save").click()
        driver.get(self.base_url + "/#/group/Eh/az")
        driver.find_element_by_xpath("//div[@id='teamMatchesWidget']/div/a").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: %s username passwd" % sys.argv[0]
        sys.exit(0)

    rankade = Rankade(sys.arg[1], sys.argv[2])
    rankade.insert_one_match({})
