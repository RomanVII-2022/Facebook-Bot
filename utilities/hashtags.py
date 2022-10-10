from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.customlog import logger


class Hashtag:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.switch_to.new_window()


    def get_landing_page(self):
        try:
            self.driver.get('https://www.all-hashtag.com/')
            logger.debug('*** Access to webpage was successful ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\hashtag.png')
            logger.debug('*** Something went wrong accessing the landing page ***')


    def generate(self, keyword):
        try:
            gen_input = self.driver.find_element(By.XPATH, "//input[@id='keyword']")
            gen_input.send_keys(keyword)
            gen_input.send_keys(Keys.RETURN)
            logger.debug('*** Keyword generation was successful ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\generate.png')
            logger.debug('*** Something went wrong generating keyword hashtags ***')
    
    
    def get_results(self):
        try:
            results = self.driver.find_element(By.XPATH, "//div[@id='copy-hashtags']").text
            self.driver.close()
            logger.debug('*** Results were gotten successfully ***')
            return results
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\results.png')
            logger.debug('*** Something went wrong getting the results ***')

        
