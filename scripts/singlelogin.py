from selenium import webdriver
import util.alerthandling as ah
from util.driversetup import DRIVER

global DRIVER
#driver = ds.setupDriver()
DRIVER.get("http://127.0.0.1/DVWA/vulnerabilities/brute")

user_path = "/html/body/div/div[3]/div/div/form/input[1]"
pass_path = "/html/body/div/div[3]/div/div/form/input[2]"
submit_path = "/html/body/div/div[3]/div/div/form/input[3]"

# try multiple passwords - differtiate typing wrongly from true brute force
DRIVER.find_element_by_xpath(user_path).send_keys("admin")
DRIVER.find_element_by_xpath(pass_path).send_keys("Password.")
DRIVER.find_element_by_xpath(submit_path).click()
DRIVER.find_element_by_xpath(user_path).send_keys("admin")
DRIVER.find_element_by_xpath(pass_path).send_keys("adminpassword")
DRIVER.find_element_by_xpath(submit_path).click()
DRIVER.find_element_by_xpath(user_path).send_keys("admin")
DRIVER.find_element_by_xpath(pass_path).send_keys("password")
DRIVER.find_element_by_xpath(submit_path).click()
