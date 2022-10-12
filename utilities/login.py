from selenium.webdriver.common.by import By
import time


class Login:
    def login_page(self, email, password):
        try:
            email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
            email_input.send_keys(email)
            self.logger.debug('*** Email was added successfully ***')
            password_input = self.driver.find_element(By.XPATH, "//input[@id='pass']")
            password_input.send_keys(password)
            self.logger.debug('*** Password was added successfully ***')
            login_btn = self.driver.find_element(By.XPATH, "//button[@name='login']")
            login_btn.click()
            self.logger.debug('*** You are logging into Facebook... ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\login.png')
            self.logger.debug('*** Something went wrong during login ***')


    def confirm_login(self):
        try:
            time.sleep(5)
            title = self.driver.title
            if title == 'Facebook':
                self.logger.debug('You have successfully accessed Facebook home page')
            else:
                self.logger.debug('Something went wrong accessing Facebook home page')
        except:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\confirmlogin.png')
            self.logger.debug('*** Somethig went wrong ***')
