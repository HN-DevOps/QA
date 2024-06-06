# Web driver manager will be used to download and setup the browsers without we have to explicitly download them.

import time  # for importing libraries for time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here

driver.get("https://ff.iot.vodafone.com.qa")  # hitting the url of prod frozen food
time.sleep(2)  # for adding some delay before closing the browser.

driver.close()  # for closing the particular window or tab
driver.quit()  # for closing the complete instant of driver

print("Done")

