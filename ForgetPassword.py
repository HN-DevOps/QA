import time  # for importing libraries for time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here

driver.get("https://ff.iot.vodafone.com.qa")
driver.maximize_window()
time.sleep(5)

Forget_pass_button = (driver.find_element(
    By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[3]/button"
)
                      .click())
time.sleep(3)
Enter_email = driver.find_element(
    By.XPATH, "/html/body/app-root/div[2]/app-login/div[2]/div/div/div[2]/form/div/input"
)
time.sleep(3)
Enter_email.send_keys("najla.87@yopmail.com")
time.sleep(3)

submit_button = (WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-login/div[2]/div/div/div[3]/button[2]"))
)
                 .click())
time.sleep(2)

ok_Button = (WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[6]/button[1]"))
)
             .click())
# Waiting for output field to be appear
time.sleep(4)
otp =input("Enter the otp received on provided email")
otp_input = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input"))
)
otp_input.send_keys(otp)

# Verify Button
Verify_button = (driver.find_element(
    By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button[1]"
)
                 .click())
time.sleep(3)
Ok_Button = (driver.find_element(
    By.XPATH,"/html/body/div[1]/div/div[6]/button[1]"
)
             .click())
time.sleep(3)

# reset pass screen

New_pass = driver.find_element(
    By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/input")
New_pass.send_keys("Aa654321@@")
NP_view = (driver.find_element(
    By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/span/i"
)
          .click())
time.sleep(2)

Confirm_Pass = driver.find_element(
    By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")
Confirm_Pass.send_keys("Aa654321@@")
CP_view = (driver.find_element(
    By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/span/i"
)
          .click())
time.sleep(2)

Reset_pass_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button"))
)
Ok_Button = (driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[6]/button[1]"
)
             .click())
time.sleep(2)

# Back to log in
#Back_to_Login_Button = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button[2]")
#Back_to_Login_Button.click()
#time.sleep(5)
# Didn't get the code?
#Code_not_received = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/a")
#Code_not_received.click()
#time.sleep(5)
