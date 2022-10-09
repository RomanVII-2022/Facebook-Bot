from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.customlog import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from utilities.hashtags import Hashtag


class Facebook:
    def __init__(self, driver=webdriver.Chrome(service=Service('C:\Program Files (x86)/chromedriver.exe')), 
    teardown=False):
        self.driver = driver
        self.teardown = teardown
        super(Facebook, self).__init__()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()


    def get_landing_page(self):
        try:
            self.driver.get('https://www.facebook.com/')
            logger.debug('*** Landing page was accessed succefully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\landingPage.png')
            logger.debug('*** Something went wrong accessing the landing page ***')


    def login_page(self, email, password):
        try:
            email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
            email_input.send_keys(email)
            logger.debug('*** Email input element was found successfully ***')
            password_input = self.driver.find_element(By.XPATH, "//input[@id='pass']")
            password_input.send_keys(password)
            logger.debug('*** Password input element was found successfully ***')
            login_btn = self.driver.find_element(By.XPATH, "//button[@name='login']")
            login_btn.click()
            logger.debug('*** Login was successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\login.png')
            logger.debug('*** Something went wrong finding an element in the login page ***')


    def menu(self):
        try:
            menu_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Menu' and @role='button']/div[2]")
            menu_btn.click()
            create_post = self.driver.find_element(By.XPATH, "//span[normalize-space()='Post']")
            create_post.click()
            logger.debug('*** Elements in the create post menu were found successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\menu.png')
            logger.debug('*** Something went wrong finding elements in create post menu ***')
       


    def create_post(self, status, imagePath):
        try:
            original_window = self.driver.current_window_handle
            hashtag = Hashtag(driver=self.driver)
            hashtag.get_landing_page()
            hashtag.generate('python')
            results = hashtag.get_results()
            
            self.driver.switch_to.window(original_window)  
            status_input = self.driver.find_element(By.XPATH, "//div[@role='textbox']")
            status_input.send_keys(status + ' ' + results)
            logger.debug('*** Caption was added successfully ***')
            #self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(imagePath)
            #logger.debug('*** Image or video was added successfully ***')
            add_photo = self.driver.find_element(By.XPATH, "//div[@aria-label='Photo/Video']")
            add_photo.click()
            self.driver.find_element(By.XPATH, "//span[contains(.,'Add Photos/Videos')]").click()
            time.sleep(10)
            pyautogui.write(imagePath)
            pyautogui.press('enter')
            logger.debug('*** Image or video was added successfully ***')
            time.sleep(10)
            post_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Post']")
            post_btn.click()
            logger.debug('*** Post was created successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\post.png')
            logger.debug('*** Something went wrong while creating post ***')

        



        