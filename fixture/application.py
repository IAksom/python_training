from selenium import webdriver
from fixture.session import SessionHelper
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
_author_ = 'Iryna'

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.session = SessionHelper(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    def create_group(self, group):
        driver = self.driver
        # init group creation
        driver.find_element_by_name("new").click()
        # create new group
        driver.find_element_by_name("group_name").click()
        # fill group form
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.head)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def destroy(self):
        self.driver.quit()

