from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pyautogui


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


    def groups(self, message, imagePath):
        groups = ['464335001194148', '119019300063018']
        for id in groups:
            self.driver.switch_to.new_window()
            self.driver.get('https://web.facebook.com/groups/' + id)
            add_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='Write something...']")
            add_btn.click()
            write = self.driver.find_element(By.XPATH, "//div[@aria-label='Create a public post…']")
            write.send_keys(message)
            photo_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Photo/Video']")
            photo_btn.click()
            time.sleep(5)
            pyautogui.write(imagePath)
            pyautogui.press('enter')
            time.sleep(10)
            post_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Post']")
            post_btn.click()
        



p = Group()
p.get_landing_page()
p.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
time.sleep(10)
p.groups('For any construction material contact us.', 'C:\pictures\chames.jpg')
