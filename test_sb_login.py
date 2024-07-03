import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def fixture_setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://saas-sbdt-dev-app-web-du-uae.azurewebsites.net/#/Login")
    driver.maximize_window()
    yield
    driver.quit()


def test_sb_login(fixture_setup):
    wait = WebDriverWait(driver, 20)

    try:
        email = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/div[1]/input")))
        email.send_keys("mujtabaaziz@yopmail.com")
        time.sleep(2)

        password = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/div[2]/input")))
        password.send_keys("Aa@123456")
        time.sleep(2)

        view_password_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                      "html > body > div:first-of-type > div > div > div:nth-of-type(2) > div > div > div > form > div:nth-of-type(2) > div > svg")))
        ActionChains(driver).move_to_element(view_password_button).click().perform()
        time.sleep(2)

        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/button")))
        ActionChains(driver).move_to_element(login_button).click().perform()
        time.sleep(2)

        select_building = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/section/div/div/div/div[3]/div/div/div/div/div/button")))
        ActionChains(driver).move_to_element(select_building).click().perform()
        time.sleep(2)

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Scroll back to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # Navigate back to the previous page
        driver.back()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        logout_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/header/nav/div/div/div[3]/form/ul/li[2]/button")))
        ActionChains(driver).move_to_element(logout_button).click().perform()
        time.sleep(2)

        assert "SB DT Twin" in driver.title
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
