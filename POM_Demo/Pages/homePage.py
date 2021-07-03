from selenium.webdriver.common.keys import Keys
class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
        #self.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[3]/a').send_keys(Keys.ENTER)