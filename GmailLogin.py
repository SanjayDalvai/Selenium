from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/Selenium/driver/chromedriver.exe")

driver.get("https://www.google.com/")

driver.maximize_window()

driver.find_element_by_link_text("Gmail").click()



driver.find_element_by_link_text('Sign in').click()

driver.find_element_by_id('identifierId').send_keys('dalvai.sanju').send_keys(Keys.ENTER)
#driver.find_element_by_link_text("Next").click()

driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

driver.close()

driver.quit()