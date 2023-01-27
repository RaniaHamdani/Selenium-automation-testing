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
global i
i = 100

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


@allure.severity(allure.severity_level.NORMAL)
class TestCandidate(unittest.TestCase):

    def test_candidate_journey(self): 
        assert True
    
        driver = webdriver.Chrome(chrome_options=opt,executable_path=r"C:\webdrivers\chromedriver.exe")

        driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/authentication?role=candidate&pid=6Dax4CnRGO3nO1f41QREIZ")
        
        login(104,driver)
        try:
            current_role = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Current Role"][id="mui-1"]')
            current_role.send_keys('software engineer')

        except:
            pytest.skip("skipping")    

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

      


        assessment = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start"]')
        assessment.click()

        submit = list(driver.find_elements(By.XPATH, '//button'))[-1] #[text()="Start assessment"]')
        submit.click()
        allure.attach(driver.get_screenshot_as_png(), name="testcandidateAssessmentScreen",
                        attachment_type = AttachmentType.PNG)
        assert True
        #get screenshot of final results
        allure.attach(driver.get_screenshot_as_png(), name="testcandidateAssessmentScreen",
                        attachment_type = AttachmentType.PNG)
        
    
            
        
@allure.severity(allure.severity_level.NORMAL)
class TestRecruiter(unittest.TestCase):

    def test_recruiter_journey(self): 
        assert True
        
        driver = webdriver.Chrome(chrome_options=opt,executable_path=r"C:\webdrivers\chromedriver.exe")

        driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/authentication?role=recruiter")
        login(105,driver)

        
        new_job =driver.find_element(By.CLASS_NAME, "landingPage_buttonContainer__znBw9")
        new_job = new_job.find_element(By.CSS_SELECTOR, "button")
        new_job.click()


        job_title = driver.find_element(By.ID, "combo-box-demo")
        job_title.send_keys("Agile coach")
        first_result= driver.find_element(By.CSS_SELECTOR, "li")
        job= first_result.get_attribute('innerHTML')
        clear = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Clear']")
        clear.click()
        driver.implicitly_wait(2)
        job_title.send_keys(str(job))



        csompetencies = ['Organisational Facilitation', 'Measurement','Methods and Tools']
        select_competencies = driver.find_element(By.CLASS_NAME, "CheckBoxRectangle_containerChecked__354fP")
        select_competencies.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
        add= driver.find_element(By.CSS_SELECTOR, 'div[class="MuiAutocomplete-root MuiAutocomplete-hasClearIcon AutoComplete_field__K8rex css-1mg75n9"]')

        add_comp = add.find_element(By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root projectDetails_button__r3wtr css-1ujsas3"]')
        add_comp.click()

        add_competency = list(driver.find_elements(By.ID, "combo-box-demo"))[1]
        add_competency.send_keys('software development')


        first_result= driver.find_element(By.CSS_SELECTOR, "li")
        print(first_result)
        comp= first_result.get_attribute('innerHTML')
        print(comp)
        clear = list(driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Clear']"))[1]
        clear.click()
        add_competency = list(driver.find_elements(By.ID, "combo-box-demo"))[1]

        driver.implicitly_wait(2)
        add_competency.send_keys(str(comp))

        next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
        next.click()

        #enter position details

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

        #select assessment

        select_assessment = list(driver.find_elements(By.CSS_SELECTOR, 'div[class="assessments_boxContainer__slM_G"]'))[8]
        select = select_assessment.find_element(By.CSS_SELECTOR, 'button')
        select.click()

        next =  driver.find_element(By.XPATH, '//button[@class="SimpleButton_general__X6MK9 SimpleButton_simple__h5FX_"]')
        next.click()

        #add question
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

        allure.attach(driver.get_screenshot_as_png(), name="testRecruiterScreen",
                        attachment_type = AttachmentType.PNG)

        assert True   
                    

@allure.severity(allure.severity_level.NORMAL)
class TestEmployee(unittest.TestCase):

    def test_employee_journey(self):  
        assert True  
    
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r"C:\webdrivers\chromedriver.exe")
        driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/authentication?role=employee&pid=14PmcFgSZQVa6JGRWl3iwi")
        login(105,driver)
        
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
        allure.attach(driver.get_screenshot_as_png(), name="testEmployeeScreen",
                        attachment_type = AttachmentType.PNG)
       
        assert True
    

@allure.severity(allure.severity_level.NORMAL)
class TestManager(unittest.TestCase):

    def test_manager_journey(self):
        assert True
        
        driver= webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
        #driver.maximize_window()
        driver.get("https://cb-smart-recruitment-front-end.azurewebsites.net/candidate/authentication?role=manager")

        email = driver.find_element(By.NAME, "email")
        email.send_keys("raniahamdeni@gmail.com")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("passwordrania")

        #click sign up
        log_in =  driver.find_element(By.XPATH, '//button[text()="Log in"]')
        log_in.click()

        driver.implicitly_wait(5)

        #create project 

        invisible = WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="CustomButton1_row__t75tY"]')))
        if invisible:
            create_project = driver.find_element(By.XPATH,'//span[@class="CustomButton1_row__t75tY"]')
            create_project.click()

        #WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="CustomButton1_general__F0qB7 CustomButton1_outline___Emeq"]'))).click()


        name = driver.find_element(By.XPATH, '//input[@placeholder="Project Name"]')
        name.send_keys('Project Name 1')

        start = driver.find_element(By.XPATH, '//input[@placeholder="mm/dd/yyyy"]')
        start.find_element(By.CSS_SELECTOR, "button").click()


        #end = list(driver.find_elements(By.XPATH, '//input[@placeholder="mm/dd/yyyy"]'))[1]
        #end.find_element(By.CSS_SELECTOR, "button").click()
        name = driver.find_element(By.XPATH, '//input[@placeholder="Project Name"]')
        name.send_keys('Project Name 1')

        start = driver.find_element(By.XPATH, '//input[@placeholder="mm/dd/yyyy"]')
        start.find_element(By.CSS_SELECTOR, "button").click()

        allure.attach(driver.get_screenshot_as_png(), name="testEmployeeScreen",
                        attachment_type = AttachmentType.PNG)
       
        assert True

        