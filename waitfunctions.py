import time  # for importing libraries for time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Functions import click_menu_option_and_wait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here

# globally defining wait time and apply it after each navigation action to wait for the page to load (implicit wait)
wait_time = 8

driver.get("https://ff.iot.vodafone.com.qa")  # hitting the url of prod frozen food

# finding element and performing action with seperate statements via storing them into variables
FFinputemail = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input").send_keys("najla.87@yopmail.com")  # email field
FFinputpassword = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys("Aa123456@")  # password field

# time.sleep(3)

FFviewpass = driver.find_element(By.CLASS_NAME, "ion-eye-disabled").click()  # for displaying the password.
FFcheckbox = driver.find_element(By.ID,"inputCheckbox")  # remember me checkbox  on login
# time.sleep(2)
if FFcheckbox.is_selected():
    print("remember me checked")
if not FFcheckbox.is_selected():
    FFcheckbox.click()
FFclicklogin = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button").click()  # clicking sign in button.
time.sleep(25)

# Define functions to perform actions and wait
# def click_menu_option_and_wait(by, XPATH):
    # option = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((by, XPATH)))
    # option.click()
    # time.sleep(wait_time)

# Explicit Wait, specifically the WebDriverWait class from Selenium WebDriver's
# ------------------------ Dashboard -----------------------
Dashboard = driver.find_element(By.CLASS_NAME,"site-menu-title").click()
time.sleep(4)

# -----------------------FMCG Management ---------------------------------
TruckManagement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/a/span/span[3]"))).click()

# in case of calling function from another file we have to use driver, argument at th beginning of by class.
History = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[2]/span/a/span/span[3]")
Territory = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[3]/span/a/span/span[3]")
Trucks = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[4]/span/a/span/span[3]")
# time.sleep(4)

# ---------------------- Drivers Module -----------------------------------

DriversModule = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/a/span/span[3]"))).click()
Driver = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[1]/span/a/span/span[3]")
Shifts = click_menu_option_and_wait(driver,By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[2]/span/a/span/span[3]")
Jobs = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[3]/span/a/span/span[3]")
DtoTAssociation = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[4]/span/a/span/span[3]")
DtoSAssociation = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[5]/span/a/span/span[3]")
Tools = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[6]/span/a/span/span[3]")
Locations = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[3]/div/span[7]/span/a/span/span[3]")

# ---------------------- Alerts Module -----------------------------------

AlertMoodule = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[5]/a/span"))).click()
Alerts = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[5]/div/span/span/a/span/span[3]")

# ---------------------- Users&Admin----------------------------------------

UsersModule = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[6]/a/span/span[3]"))).click()
UsersTab = click_menu_option_and_wait(driver,By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[6]/div/span[1]/span/a/span/span[3]")
accessGroups = click_menu_option_and_wait(driver, By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[6]/div/span[2]/span/a/span/span[3]")

# ----------------------- Reports -----------------------------------------

Reports = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[7]/a/span/span[3]"))).click()
ReportsTab = click_menu_option_and_wait(driver, By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[7]/div/span/span/a/span/span[3]")

# ----------------------Logout ---------------------------------------------

ProfileIcon = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-dashboard/app-header/nav/div[2]/div[1]/ul[2]/li[3]/a/span/img"))).click()
logout = click_menu_option_and_wait(driver, By.XPATH,"/html/body/app-root/div[2]/app-dashboard/app-header/nav/div[2]/div[1]/ul[2]/li[3]/ul/li[2]/a")

def wait_for_element_to_be_clickable():
    return None