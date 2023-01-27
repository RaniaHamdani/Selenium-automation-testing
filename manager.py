from typing import ByteString
from selenium.webdriver.chrome.options import Options
import unittest
import allure
from allure_commons.types import AttachmentType

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#from seleniumbase import BaseCase

    

global driver

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

def login(i,driver):
    email_string= "raniacandidate"+str(i)+"@gmail.com"
    email = driver.find_element(By.NAME, "email")
    email.send_keys(email_string)
    password_string= "raniacandidate"+str(i)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(password_string)

    log_in =  driver.find_element(By.XPATH, '//button[text()="Log in"]')
    log_in.click()

    driver.implicitly_wait(5)


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
     
    email_string = "raniacandidate"+str(i)+"@gmail.com"

    Email = driver.find_element(By.NAME,"register_email")
    Email.send_keys(email_string)
    
    password_string= "raniacandidate"+str(i)

    Password = driver.find_element(By.NAME,"register_password")
    Password.send_keys(password_string)

    Confirm_Password = driver.find_element(By.NAME,"confirm")
    Confirm_Password.send_keys(password_string)

    Phone = driver.find_element(By.NAME,"phone")
    Phone.send_keys(27676427)

    #click sign up
    sign_up =  driver.find_element(By.XPATH, '//button[text()="Sign up"]')
    sign_up.click()


@allure.severity(allure.severity_level.NORMAL)
class TestCandidate(unittest.TestCase):


    def test_candidate_journey(self):
        
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r"C:\webdrivers\chromedriver.exe")
        driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/authentication?role=candidate&pid=6Dax4CnRGO3nO1f41QREIZ")
        signup(4,driver)
        current_role = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Current Role"][id="mui-1"]')
        current_role.send_keys('software engineer')
        inputs= list( driver.find_elements(By.CSS_SELECTOR,'div[role="button"]'))

        years = inputs[0]
        years.click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        element.click() 

        diploma = inputs[1]
        diploma.click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        element.click()
        #driver.find_element(By.CSS_SELECTOR, 'li').click()

        citizenship = inputs[2]
        citizenship.click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        element.click()
        #driver.find_element(By.CSS_SELECTOR, 'li').click()
        #driver.implicitly_wait(5)



        currency = inputs[3]
        currency.click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li')))
        element.click()
        #driver.find_element(By.CSS_SELECTOR, 'li').click()
        #driver.implicitly_wait(5)

        university = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="University"]' )
        university.send_keys('university of tunisia')

        min_sal = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Min Annual Salary"]' )
        min_sal.send_keys(8000)

        max_sal = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Max Annual Salary"]' )
        max_sal.send_keys(9000)

        photo = driver.find_element(By.XPATH, '//input[@type="file"]')
        #photo.click()
        photo.send_keys(r'C:\Users\21627\Desktop\nour.jpg')


        cv = list(driver.find_elements(By.XPATH, '//input[@type="file"]'))[1]
        cv.send_keys(r'C:\Users\21627\Desktop\cv.pdf')

        start =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
        start.click()

        confirm = driver.find_element(By.XPATH, '//span[text()="I confirm"]')
        confirm.click()

        driver= webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
        #driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/landing3")
        checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="toggle"]')))
        checkbox.click()

        #start = driver.find_element(By.XPATH, '//span[text()="Start assessment"]')

        #start = driver.find_element(By.XPATH, '//button[text()="Start assessment"]')
        #start.click()
        time.sleep(5)
        assessment = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start assessment"]')
        assessment.click()
        time.sleep(5)

        assessment = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start assessment"]')
        assessment.click()
        time.sleep(150)
        #recording = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Stop Recording"]')))
        #recording.click()

        assessment = driver.find_element(By.XPATH, '//span[text()="Next"]')
        assessment.click()

        #start assessment
        assessment = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start"]')
        assessment.click()

        submit = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start assessment"]')
        submit.click()

        #get screenshot of final results
        allure.attach(driver.get_screeshot_as_png(), name="testcandidateScreen",
                        attachment_type = AttachmentType.PNG)






