from selenium import webdriver
from POM_Demo.Pages.Login import LoginPage
from POM_Demo.Pages.homePage import HomePage
import time

driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/Selenium/driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
login = LoginPage(driver)
login.enter_username("Admin")
login.enter_password("admin123")
login.click_login()


homePage = HomePage(driver)
homePage.click_welcome()
homePage.click_logout()


#driver.find_element_by_id("txtUsername").send_keys("Admin")

#driver.find_element_by_id("txtPassword").send_keys("admin123")
#driver.find_element_by_id("btnLogin").click()
#driver.find_element_by_id("welcome").click()
#driver.find_element_by_link_text("Logout").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")