import time  # for importing libraries for time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By # by is the class in selenium so for this imported By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def fixture_setup(): # after fixture what we will be writing will execute before testcase.
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here
    driver.get("https://ff.iot.vodafone.com.qa")  # hitting the url of prod frozen food
    driver.maximize_window()  # for maximizing the window
    yield  # after yield what we will be writing will execute after testcase.
    driver.close()

def test_login(fixture_setup):
    FFinputemail = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")  # email field
    FFinputemail.send_keys("najla.87@yopmail.com")
    FFinputpassword = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")  # password field
    FFinputpassword.send_keys("Aa123456@")
    time.sleep(3)

    FFviewpass = driver.find_element(By.CLASS_NAME, "ion-eye-disabled").click()  # for displaying the password.
    FFcheckbox = driver.find_element(By.ID,"inputCheckbox")  # remember me checkbox  on login
    time.sleep(2)
    if FFcheckbox.is_selected():
         print("remember me checked")
    if not FFcheckbox.is_selected():
        FFcheckbox.click()
    FFclicklogin = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")  # clicking sign in button.
    FFclicklogin.click()
    time.sleep(25)
def test_invalid_creds (fixture_setup):
    ffinputemail = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")
    ffinputemail.send_keys("najla66@yopmail.com")
    ffinputpassword = driver.find_element(By.XPATH,
                                          "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")
    ffinputpassword.send_keys("@A783234")
    ffclicklogin = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")
    ffclicklogin.click()
    time.sleep(3)
    assert "Invalid username or password" in driver.page_source  # using assert because this is what am expecting it to behave

def test_empty_fields(fixture_setup):
    ffinputemail = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")  # email field
    ffinputemail.send_keys("")
    ffinputpassword = driver.find_element(By.XPATH,
                                          "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")  # password field
    ffinputpassword.send_keys("")
    ffclicklogin = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")  # clicking sign in button.
    ffclicklogin.click()
    assert not ffclicklogin.is_enabled(), "login button enable with empty fields"  # this is not what i am expecting, checks that the login button is not enabled

def test_empty_email_field(fixture_setup):
    ffinputemail = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")
    ffinputemail.send_keys("")
    ffinputpassword = driver.find_element(By.XPATH,
                                          "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")
    ffinputpassword.send_keys("Aa12345678@")
    ffclicklogin = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")
    ffclicklogin.click()
    assert "enter email address" in driver.title

def test_empty_password_field(fixture_setup):

    ffinputemail = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")
    ffinputemail.send_keys("najla.87@yopmail.com")
    ffinputpassword = driver.find_element(By.XPATH,
                                          "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div[1]/input")
    ffinputpassword.send_keys("ijhgj")
    ffclicklogin = driver.find_element(By.XPATH,
                                       "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")
    ffclicklogin.click()
    assert "invalid password" in driver.title

    #assert "Cold Chain" in driver.title  # Check if browser had name "cold chain or not" is present in the page title
    #assert "Dashboard" in driver.page_source  # Check if it named as "dashboard" after login is present in the page source.