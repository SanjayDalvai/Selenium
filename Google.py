from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Import time
driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/Selenium/driver/chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element_by_name("q").send_keys("python")
#driver.find_element_by_name(self, btnK).click()
driver.find_element_by_name("q").send_keys(Keys.ENTER)
#driver.get_screenshot_as_file("D:\Python ImageTest\image1.png")
#driver.find_element_by_partial_link_text("LinkedIn Login").click()
#driver.find_element_by_id("username").send_keys("enter your username")
#driver.find_element_by_id("password").send_keys("enter your password”)
#driver.find_element_by_tag_name("button").click()
#time.sleep(5)
#print(driver.title)
#print(driver.current_url)
driver.close()
driver.quit()