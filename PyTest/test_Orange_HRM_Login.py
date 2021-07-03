from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure
import time
import pytest

class Test_OHRM():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/Selenium/driver/chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        yield
        driver.find_element_by_id("welcome").click()
        driver.implicitly_wait(5)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[3]/a').send_keys(Keys.ENTER)

      #  // *[ @ id = "welcome"]
        time.sleep(5)
        driver.close()
        driver.quit()
        print("Test complete")

    def test_login(self, test_setup):
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x = driver.title
        assert x == "OrangeHRM"
    # def test_logout():

    # setup()
    # login()
    # logout()
