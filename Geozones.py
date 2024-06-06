import time  # for importing libraries for time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Functions import click_menu_option_and_wait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here

wait_time = 8 # implicit time

driver.get("https://ff.iot.vodafone.com.qa")  # hitting the url of prod frozen food

# finding element and performing action with seperate statements via storing them into variables
FFinputemail = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input").send_keys("najla.87@yopmail.com")  # email field
FFinputpassword = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys("Aa123456@")  # password field
time.sleep(3)
FFviewpass = driver.find_element(By.CLASS_NAME, "ion-eye-disabled").click()  # for displaying the password.
FFcheckbox = driver.find_element(By.ID,"inputCheckbox")  # remember me checkbox  on login
time.sleep(2)
if FFcheckbox.is_selected():
    print("remember me checked")
if not FFcheckbox.is_selected():
    FFcheckbox.click()
FFclicklogin = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button").click()  # clicking sign in button.
time.sleep(25)

# ------------------------ Dashboard -----------------------
Dashboard = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"site-menu-title")))
time.sleep(4)

# -----------------------FMCG Management ---------------------------------
TruckManagement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/a/span/span[3]"))).click()
time.sleep(4)
# in case of calling function from another file we have to use driver, argument at th beginning of by class.
History = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[2]/span/a/span/span[3]")
Territory = click_menu_option_and_wait(driver, By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/span[2]/div/span[3]/span/a/span/span[3]")
# Finding button element and wait for it to be clickable
add_zone = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > div:nth-child(2) > app-dashboard > div > div > app-manage-geozone > div.full-open-sidebar.page-content.container-fluid > div.row.card-group-row > div.col-lg-4.card-group-row__col > div > div.panel-body.padding-15 > div.col-lg-12.ng-star-inserted > button"))).click()
zone_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "tryFormID")))  # Waiting for form to be appeared

# performing actions entering data in form
time.sleep(4)
Name = zone_form.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[1]/div/div/input")
Name.send_keys("Automated zone")
time.sleep(4)
# clicking on vehicles' dropdown.
vehicle = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[2]/div/p-multiselect/div/div[2]/span")
vehicle.click()
time.sleep(3)
# finding vehicles which we need
vehicle_checkboxes = driver.find_elements(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[2]/div/p-multiselect/div/div[4]/div[2]/ul/p-multiselectitem/li")
time.sleep(2)
Select_Truck = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[2]/div/p-multiselect/div/div[4]/div[2]/ul/p-multiselectitem[4]/li")
if not Select_Truck.is_selected():
    Select_Truck.click()
# closing dropdown
time.sleep(2)
close_dropdown = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[2]/div/p-multiselect/div/div[4]/div[1]/a/span")
close_dropdown.click()
time.sleep(2)
# Access Type Dropdown
access_type = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[3]/div/p-dropdown/div/div[2]/span")
access_type.click()
time.sleep(2)

option = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[3]/div/p-dropdown/div/div[4]/div/ul/p-dropdownitem[1]/li")
option.click()
time.sleep(2)
instructions = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[4]/div/div/textarea")
time.sleep(2)
instructions.send_keys("This zone area is powered by Vodafone vehicles only")
time.sleep(2)

# Find and click on the "draw zone" button to activate drawing mode
draw_zone_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[2]/div")))
# Verify that the button is visible and enabled
if draw_zone_button.is_displayed() and draw_zone_button.is_enabled():
    draw_zone_button.click()
else:
    print("Draw zone button is not visible and enabled")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
time.sleep(2)
button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[6]/button[1]").click()
time.sleep(4)
Close_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[2]/button[1]"))).click()
time.sleep(4)

# Edit the form.
createdZone = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[5]/button[1]")
time.sleep(2)
createdZone.click()
time.sleep(2)

UpdatingNameFirst = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[1]/div/div/input")
Value = UpdatingNameFirst.get_attribute("FORBIDDEN-ZONE")
time.sleep(2)
UpdatingName_second =driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/div/div[1]/div/div/input")
time.sleep(2)
UpdatingName_second.clear()
time.sleep(2)
UpdatingName_second.send_keys("zone update")
time.sleep(2)

Update_button = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-dashboard/div/div/app-manage-geozone/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
time.sleep(4)