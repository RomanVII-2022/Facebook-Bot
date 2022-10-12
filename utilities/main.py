from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.login import Login
from utilities.pagepost import Page
from utilities.grouppost import Group
from utilities.customlog import Logger


class Facebook(Login, Page, Group):
    def __init__(self, driver=webdriver.Chrome(service=Service('C:\Program Files (x86)/chromedriver.exe')), 
    teardown=False):
        self.driver = driver
        self.teardown = teardown
        self.logger = Logger.logger_gen()
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
            self.logger.debug('*** Landing page was accessed succefully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\landingPage.png')
            self.logger.debug('*** Something went wrong accessing the landing page ***')


    def pagepost(self):
        self.get_landing_page()
        self.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
        self.confirm_login()
        self.menu()
        self.create_post('construction', 'soil', 'C:\pictures\phone.jpg')

    def post_like_and_comment(self):
        self.get_landing_page()
        self.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
        self.confirm_login()
        self.like_and_comment_page('Nice product')


    def grouppost(self):
        self.get_landing_page()
        self.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
        self.confirm_login()
        self.groups('Hello World', 'C:\pictures\chames.jpg')


    def group_like_and_comment(self):
        self.get_landing_page()
        self.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
        self.confirm_login()
        self.like_and_comment_group('Nice product')




        



        