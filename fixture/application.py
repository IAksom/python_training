from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
_author_ = 'Iryna'

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login(self, username='admin', password='secret'):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(u"//input[@value='Увійти']").click()

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

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"Вийти").click()

    def destroy(self):
        self.driver.quit()

