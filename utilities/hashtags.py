from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Hashtag:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.switch_to.new_window()


    def get_landing_page(self):
        self.driver.get('https://www.all-hashtag.com/')

    def generate(self, keyword):
        gen_input = self.driver.find_element(By.XPATH, "//input[@id='keyword']")
        gen_input.send_keys(keyword)
        gen_input.send_keys(Keys.RETURN)
    def get_results(self):
        results = self.driver.find_element(By.XPATH, "//div[@id='copy-hashtags']").text
        self.driver.close()
        return results
        
