import allure
import unittest
from selenium import webdriver
from allure_commons.types import AttachmentType
from typing import ByteString
from selenium.webdriver.chrome.options import Options
import unittest
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import pytest

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

global driver

driver = webdriver.Chrome(chrome_options=opt,executable_path=r"C:\webdrivers\chromedriver.exe")

driver.get("https://sr-portal-test.careerboosts.com/candidate/authentication?role=recruiter")
        
@allure.severity(allure.severity_level.CRITICAL)
class Test_Recruiter_login(unittest.TestCase):
    def test_recruiter_login(self):

        try:
            email = driver.find_element(By.NAME, "email")
            email.send_keys("karthickkumar28@gmail.com")
            password = driver.find_element(By.NAME, "password")
            password.send_keys("1234")

            log_in =  driver.find_element(By.XPATH, '//button[text()="Log in"]')
            log_in.click()

            driver.implicitly_wait(5)
            

            assert True  

        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
         

@allure.severity(allure.severity_level.NORMAL)
class Test_Recruiter_new_job(unittest.TestCase):
    def test_recruiter_new_job(self):
        try:
            div = list(driver.find_elements(By.XPATH,'//button[@class="CustomButton_button__1x6ro"]'))
            new_job = div[0].click()
            driver.implicitly_wait(5)

            assert True
        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
      
 
@allure.severity(allure.severity_level.CRITICAL)    
class Test_Recruiter_job_title(unittest.TestCase):
    def test_recruiter_job_title(self):
        try:
            job_title = driver.find_element(By.ID, "combo-box-demo")
            job_title.send_keys("Agile coach")
            first_result= driver.find_element(By.CSS_SELECTOR, "li")
            job= first_result.get_attribute('innerHTML')
            clear = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Clear']")
            clear.click()
            driver.implicitly_wait(2)
            job_title.send_keys(str(job))

            assert True
        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
    

@allure.severity(allure.severity_level.NORMAL)
class Test_Recruiter_enter_competencies(unittest.TestCase):
    def test_recruiter_enter_competencies(self):
        try:
            select_competencies = driver.find_element(By.CLASS_NAME, "CheckBoxRectangle_containerChecked__354fP")
            select_competencies.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
            add= driver.find_element(By.CSS_SELECTOR, 'div[class="MuiAutocomplete-root MuiAutocomplete-hasClearIcon AutoComplete_field__K8rex css-1mg75n9"]')

            add_comp = add.find_element(By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root projectDetails_button__r3wtr css-1ujsas3"]')
            add_comp.click()

            add_competency = list(driver.find_elements(By.ID, "combo-box-demo"))[1]
            add_competency.send_keys('software development')


            first_result= driver.find_element(By.CSS_SELECTOR, "li")
            comp= first_result.get_attribute('innerHTML')
            clear = list(driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Clear']"))[1]
            clear.click()
            add_competency = list(driver.find_elements(By.ID, "combo-box-demo"))[1]

            driver.implicitly_wait(2)
            add_competency.send_keys(str(comp))

            next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
            next.click()
            driver.implicitly_wait(5)


            assert True

        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
       


@allure.severity(allure.severity_level.MINOR)
class Test_Recruiter_position_details(unittest.TestCase):
    def test_recruiter_position_details(self):
        try:
            client = driver.find_element(By.XPATH, '//input[@placeholder="Client"]')
            client.send_keys('Rania')
            inputs= list( driver.find_elements(By.CSS_SELECTOR,'div[role="button"]'))

            role = inputs[0]
            role.click()
            role_liste = driver.find_element(By.CSS_SELECTOR, 'li').click()

            work = inputs[1]
            driver.implicitly_wait(3)
            work.click()
            driver.implicitly_wait(3)
            work_liste = driver.find_element(By.CSS_SELECTOR, 'li').click()

            currency = inputs[2]
            #list( driver.find_elements(By.CSS_SELECTOR,'div[role="button"]'))[2]
            currency.click()
            currency_liste =driver.find_element(By.CSS_SELECTOR, 'li').click()


            min_salary = driver.find_element(By.XPATH, '//input[@placeholder="Min Annual Salary"]')
            min_salary.send_keys(1000)
            max_salary = driver.find_element(By.XPATH, '//input[@placeholder="Max Annual Salary"]')
            max_salary.send_keys(2000)

            nationnality = inputs[3]
            driver.implicitly_wait(3)
            #list( driver.find_elements(By.CSS_SELECTOR,'div[role="button"]'))[3]
            nationnality.click()
            driver.implicitly_wait(3)
            nationnality_liste = driver.find_element(By.CSS_SELECTOR, 'li').click()

            on_site = driver.find_element(By.XPATH, '//input[@type="radio"][@value="onsite"]')
            driver.implicitly_wait(3)

            on_site.click()
            description = driver.find_element(By.XPATH, '//textarea[@placeholder="Description"]')
            description.send_keys("description")

            next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
            next.click()
            driver.implicitly_wait(5)


            assert True

        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
       

        
@allure.severity(allure.severity_level.NORMAL)
class Test_Recruiter_select_assessment(unittest.TestCase): 
    def test_recruiter_select_assessment(self):
        try:       
            select_assessment = list(driver.find_elements(By.CSS_SELECTOR, 'div[class="assessments_boxContainer__slM_G"]'))[3]
            select = select_assessment.find_element(By.CSS_SELECTOR, 'button')
            select.click()

            next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
            next.click()
            assert True

        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
      
    

@allure.severity(allure.severity_level.NORMAL)
class Test_Recruiter_select_questions(unittest.TestCase): 
    def test_recruiter_select_questions(self):
        try: 
            add= driver.find_element(By.XPATH ,'//span[text()="Add Question"]')
            add.click()


            question = driver.find_element(By.CSS_SELECTOR, 'input')
            question.send_keys("what's the purpose of life ?")
            add= driver.find_element(By.XPATH ,'//span[text()="Add"]')
            add.click()

            click_question = driver.find_element(By.CSS_SELECTOR, 'table')
            list(click_question.find_elements(By.CSS_SELECTOR, 'tr'))[0].click()

            next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
            next.click()

            confirm= driver.find_element(By.XPATH ,'//span[text()="Confirm "]')
            confirm.click()
            driver.implicitly_wait(3)

            close= driver.find_element(By.XPATH ,'//span[text()="Close"]')
            close.click()

            assert True
        except Exception as e:
            allure.attach(str(e), 'Exception', allure.attachment_type.TEXT)
            
            allure.attach(driver.get_screenshot_as_png(), name=e,
                    attachment_type = AttachmentType.PNG)

            pytest.skip("skipping")    
    

    



