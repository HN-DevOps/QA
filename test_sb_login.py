import time  # for importing libraries for time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # library for performing mouse actions
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def fixture_setup():  # after fixture what we will be writing will execute before testcase.
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here
    driver.get("https://new-app-sbtwin-uae.azurewebsites.net/")  # hitting the url
    driver.maximize_window()  # for maximizing the window
    yield  # after yield what we will be writing will execute after testcase.
    driver.close()

# def scroll_to_element(element):
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)

def test_sb_login(fixture_setup):
    wait = WebDriverWait(driver, 10)
    time.sleep(4)

    email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/input")))
    time.sleep(4)
    email.send_keys("abdullah.amer@hypernymbiz.com")
    time.sleep(4)

    password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[2]/input")
    time.sleep(4)
    # scroll_to_element(password)  # scrolling to password field
    password.send_keys("P2HqGITNMkQ(")
    time.sleep(4)

    view_password_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div.LoginPresentation_loginWrapper__tX6Rr > div > div > form > div:nth-child(2) > div")))
    time.sleep(4)
    # scroll_to_element(view_password_button)
    ActionChains(driver).move_to_element(view_password_button).click().perform()  # for moving cursor to perform action
    time.sleep(2)

    # remember_me_checkbox = driver.find_element(By.ID, "id_remember_me")
    # if not remember_me_checkbox.is_selected():
        # remember_me_checkbox.click()

    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/button")
    time.sleep(4)
    # scroll_to_element(login_button)
    ActionChains(driver).move_to_element(login_button).click().perform()  # for moving cursor to perform action
    time.sleep(4)

    select_building = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/section[1]/div/div/div/div/div[1]/div/div/div/button")))
    time.sleep(2)
    ActionChains(driver).move_to_element(select_building).click().perform()
    time.sleep(3)

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Scroll back to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # for navigating back to prevoius page.
    driver.back()
    time.sleep(3)

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/header/nav/div/div/div[3]/form/ul/li[1]/button")))
    time.sleep(3)
    # scroll_to_element(logout_button)
    ActionChains(driver).move_to_element(logout_button).click().perform()

    time.sleep(5)
    assert "SB DT Twin" in driver.title
