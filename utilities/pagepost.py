from selenium.webdriver.common.by import By
import time
from utilities.hashtags import Hashtag
import pyautogui
from selenium.webdriver.common.keys import Keys


class Page:
    def menu(self):
        try:
            time.sleep(10)
            menu_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Menu' and @role='button']/div[2]")
            menu_btn.click()
            self.logger.debug('*** Menu button was clicked successfully ***')
            create_post = self.driver.find_element(By.XPATH, "//span[normalize-space()='Post']")
            create_post.click()
            self.logger.debug('*** Create post pop up was accessed successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\menu.png')
            self.logger.debug('*** Something went wrong while finding create post menu ***')


    def create_post(self, status, keyword, imagePath):
        try:
            original_window = self.driver.current_window_handle
            hashtag = Hashtag(driver=self.driver)
            hashtag.get_landing_page()
            hashtag.generate(keyword)
            results = hashtag.get_results()

            self.driver.switch_to.window(original_window)  
            status_input = self.driver.find_element(By.XPATH, "//div[contains(@aria-label,'on your mind,')]")
            status_input.send_keys(status + ' ' + results)
            self.logger.debug('*** Post caption was added successfully ***')
            add_photo = self.driver.find_element(By.XPATH, "//div[@aria-label='Photo/Video']")
            add_photo.click()
            self.driver.find_element(By.XPATH, "//span[contains(.,'Add Photos/Videos')]").click()
            time.sleep(5)
            pyautogui.write(imagePath)
            pyautogui.press('enter')
            self.logger.debug('*** Image was added successfully ***')
            time.sleep(10)
            post_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Post']")
            post_btn.click()
            self.logger.debug('*** Post was created and posted successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\createpost.png')
            self.logger.debug('*** Something went wrong while creating post ***')



    def like_and_comment_page(self, comment):
        try:
            time.sleep(5)
            like_btn = self.driver.find_element(By.XPATH, "//div[@role='feed']//div[@aria-label='Like']")
            like_btn.click()
            self.logger.debug('*** Post was liked successfully ***')
            write_comment = self.driver.find_element(By.XPATH, "//div[@aria-label='Write a comment']")
            write_comment.send_keys(comment)
            write_comment.send_keys(Keys.RETURN)
            self.logger.debug('*** Coment was added successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\comment.png')
            self.logger.debug('*** Something went wrong while liking and commenting on post ***')



