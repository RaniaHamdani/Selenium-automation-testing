from selenium.webdriver.chrome.options import Options
import unittest
import ipytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from seleniumbase import BaseCase
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })


def signup(i,driver):

    sign_up =  driver.find_element(By.XPATH, '//button[text()="Sign up!"]')
    sign_up.click()

    driver.implicitly_wait(3)

    First_Name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    First_Name.send_keys("Rania")

    Middle_Name = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
    Middle_Name.send_keys("Rany")

    Last_Name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    Last_Name.send_keys("Hamdani")
     
    email_string = "raniaemployee"+str(i)+"@gmail.com"

    Email = driver.find_element(By.NAME,"register_email")
    Email.send_keys(email_string)
    
    password_string= "raniaemployee"+str(i)

    Password = driver.find_element(By.NAME,"register_password")
    Password.send_keys(password_string)

    Confirm_Password = driver.find_element(By.NAME,"confirm")
    Confirm_Password.send_keys(password_string)

    Phone = driver.find_element(By.NAME,"phone")
    Phone.send_keys(27676427)

    #click sign up
    sign_up =  driver.find_element(By.XPATH, '//button[text()="Sign up"]')
    sign_up.click()

def login(i,driver):
    email_string= "raniaemployee"+str(i)+"@gmail.com"
    email = driver.find_element(By.NAME, "email")
    email.send_keys(email_string)
    password_string= "raniaemployee"+str(i)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(password_string)

    log_in =  driver.find_element(By.XPATH, '//button[text()="Log in"]')
    log_in.click()

    driver.implicitly_wait(5)

@allure.severity(allure.severity_level.NORMAL)
class TestCandidate(unittest.TestCase):

    def test_employee_journey(self):     
    
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r"C:\webdrivers\chromedriver.exe")
        driver.get("*********")
        #signup(1,driver)
        signup(1,driver)
        
        group = driver.find_element(By.NAME, "group")
        group.click()
        group.send_keys(3)
        #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        #element.click() 

        language = driver.find_element(By.NAME, "language")
        language.click()
        language.send_keys("English")
        #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        #element.click() 

        submit= driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        submit.click()

        driver.implicitly_wait(5)
        
        assessment = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Start assessment"]')))
        assessment.click()

        time.sleep(5)
        start= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Start "]')))
        start.click()

        assert True

