_author_ = 'Iryna'

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username='admin', password='secret'):
        driver = self.app.driver
        driver.get("http://localhost/addressbook/group.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(u"//input[@value='Увійти']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text(u"Вийти").click()