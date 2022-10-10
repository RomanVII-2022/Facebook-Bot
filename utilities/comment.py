from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Group:
    def __init__(self, driver=webdriver.Chrome(service=Service('C:\Program Files (x86)/chromedriver.exe'))):
        self.driver = driver
        super(Group, self).__init__()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)


    def get_landing_page(self):
        try:
            self.driver.get('https://www.facebook.com/')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\landingPage.png')


    def login_page(self, email, password):
        try:
            email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
            email_input.send_keys(email)
            password_input = self.driver.find_element(By.XPATH, "//input[@id='pass']")
            password_input.send_keys(password)
            login_btn = self.driver.find_element(By.XPATH, "//button[@name='login']")
            login_btn.click()
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\login.png')


    def comment(self, comment):
        write_comment = self.driver.find_element(By.XPATH, "//div[@aria-label='Write a comment']")
        write_comment.send_keys(comment)
        write_comment.send_keys(Keys.RETURN)

        
            
        

p = Group()
p.get_landing_page()
p.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
time.sleep(10)
p.comment('Tunnel Vision')