import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Define functions to perform actions and wait and calling them in wait functions file
def click_menu_option_and_wait(driver, by, XPATH, wait_time=8):
    option = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((by, XPATH)))
    option.click()
    time.sleep(wait_time)
