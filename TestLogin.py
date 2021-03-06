# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username='admin', password='secret')
        self.create_group(driver, name="testtest", head="23", footer="15")
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username='admin', password='secret')
        self.create_group(driver, name="", head="", footer="")
        self.return_to_groups_page(driver)
        self.logout(driver)

    def create_group(self, driver, name, head, footer):
        # init group creation
        driver.find_element_by_name("new").click()
        # create new group
        driver.find_element_by_name("group_name").click()
        # fill group form
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(head)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(footer)
        # submit group creation
        driver.find_element_by_name("submit").click()

    def return_to_groups_page(self, driver):
        # return to groups page
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text(u"Вийти").click()

    def login(self, driver, username='admin', password='secret'):
        # login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(u"//input[@value='Увійти']").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/addressbook/group.php")

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
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
