from selenium import webdriver
import util.alerthandling as ah
from util.driversetup import DRIVER

global DRIVER

DRIVER.get("http://127.0.0.1/vulnerabilities/xss_d")
#driver.close()
