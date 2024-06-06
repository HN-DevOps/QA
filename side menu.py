import time  # for importing libraries for time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#from waitfunctions import wait_for_element_to_be_clickable

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here

# globally defining wait time and apply it after each navigation action to wait for the page to load (implicit wait)
wait_time = 5

driver.get("https://ff.iot.vodafone.com.qa")  # hitting the url of prod frozen food

# below statement will find the email input field in Frozen food
# finding element and performing action with single statement.
# driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input").send_keys("najlashaujaat@gmail.com")

# finding element and performing action with seperate statements via storing them into variables
FFinputemail = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")  # email field
FFinputemail.send_keys("najla.87@yopmail.com")
FFinputpassword = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")  # password field
FFinputpassword.send_keys("Aa123456@")
# time.sleep(3)

FFviewpass = driver.find_element(By.CLASS_NAME, "ion-eye-disabled").click()  # for displaying the password.

FFcheckbox = driver.find_element(By.ID,"inputCheckbox")  # remember me checkbox  on login
# time.sleep(2)
if FFcheckbox.is_selected():
    print("remember me checked")
if not FFcheckbox.is_selected():
    FFcheckbox.click()
FFclicklogin = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")  # clicking sign in button.
FFclicklogin.click()

time.sleep(25)

#menu = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/app-header/nav/div[2]/div[1]/ul[1]/li[1]/a/i")
#time.sleep(3)
#if not menu.is_selected():
 #   menu.click()
#if menu.is_selected():
 #   print("side menu present")


# Define functions to perform actions and wait
#def click_menu_option_and_wait(by, XPATH):
   # option = wait_for_element_to_be_clickable(by, XPATH)
    #option.click()
    #time.sleep(wait_time)

# Explicit Wait, specifically the WebDriverWait class from Selenium WebDriver's

Dashboard = driver.find_element(By.CLASS_NAME,"site-menu-title").click()
# time.sleep(4)
# -----------------------FMCG Managment ---------------------------------
TruckManagement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/a/span/span[3]"))).click()
# time.sleep(4)
History = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[2]/span/a/span/span[3]").click()
# time.sleep(4)
Territory = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[3]/span/a/span/span[3]").click()
# time.sleep(5)
ManageTrucks = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[4]/span/a/span/span[3]").click()
# time.sleep(4)
# ---------------------- Drivers Module -----------------------------------

DriversManagement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/a/span/span[3]"))).click()
# time.sleep(4)
Driver = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[1]/span/a/span/span[3]").click()
# time.sleep(5)
Shifts = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[2]/span/a/span/span[3]").click()
# time.sleep(5)
Jobs = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[3]/span/a/span/span[3]").click()
# time.sleep(5)
DtoTAssociation = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[4]/span/a/span/span[3]").click()
# time.sleep(5)
DtoSAssociation = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[5]/span/a/span/span[3]").click()
# time.sleep(5)
Tools = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[6]/span/a/span/span[3]").click()
# time.sleep(5)
Locations = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[7]/span/a/span/span[3]").click()
#time.sleep(5)