from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui


class Group:
    def groups(self, message, imagePath):
        try:
            groups = ['464335001194148', '119019300063018']
            for id in groups:
                self.driver.switch_to.new_window()
                self.driver.get('https://web.facebook.com/groups/' + id)
                add_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='Write something...']")
                add_btn.click()
                self.logger.debug('*** Group was accessed successfully ***')
                write = self.driver.find_element(By.XPATH, "//div[@aria-label='Create a public post…']")
                write.send_keys(message)
                self.logger.debug('*** Message was added successfully ***')
                photo_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Photo/Video']")
                photo_btn.click()
                time.sleep(5)
                pyautogui.write(imagePath)
                pyautogui.press('enter')
                self.logger.debug('*** Image was added successfully ***')
                time.sleep(10)
                post_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Post']")
                post_btn.click()
                self.logger.debug('*** Post was posted successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\groups.png')
            self.logger.debug('*** Something went wrong while posting to group ***')
        

    def like_and_comment_group(self, comment):
        try:
            groups = ['464335001194148', '119019300063018']
            for id in groups:
                self.driver.switch_to.new_window()
                self.driver.get('https://web.facebook.com/groups/' + id)
                time.sleep(5)
                like_btn = self.driver.find_element(By.XPATH, "//div[@aria-label='Like']")
                like_btn.click()
                self.logger.debug('*** Post was liked successfully ***')
                write_comment = self.driver.find_element(By.XPATH, "//div[contains(@aria-label,'Write')]")
                write_comment.send_keys(comment)
                write_comment.send_keys(Keys.RETURN)
                self.logger.debug('*** Comment was added successfully ***')
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\likeandcomment.png')
            self.logger.debug('*** Something went wrong accessing the landing page ***')


    def message_members(self, text):
        try:
            self.driver.switch_to.new_window()
            self.driver.get('https://web.facebook.com/groups/119019300063018/members')
            time.sleep(10)
            members = self.driver.find_elements(By.XPATH, "(//div[@role='list'])[5]/div")
            members_no = len(members) + 1
            print(members_no)
            for i in range(1, members_no):
                profile= self.driver.find_element(By.XPATH, "(//div[@role='list'])[5]/div["+str(i)+"]//a[@role='link']")
                action = ActionChains(self.driver)
                action.move_to_element(profile).perform()
                message = self.driver.find_element(By.XPATH, "//div[@aria-label='Message']")
                action.move_to_element(message).click().perform()
                self.logger.debug('*** Message button was clicked successfully ***')
                time.sleep(10)
                input_text = self.driver.find_element(By.XPATH, "//div[@data-testid='mwchat-tabs']//div[@aria-label='Message']")
                input_text.send_keys(text)
                input_text.send_keys(Keys.RETURN)
                self.logger.debug('*** Message was inputed successfully ***')
                time.sleep(10)
                close = self.driver.find_element(By.XPATH, "(//div[@aria-label='Close chat'])[1]")
                close.click()
                self.logger.debug('*** Message to member was sent successfully***')
                time.sleep(10)
        except Exception as e:
            self.driver.save_screenshot('C:\\facebook\\utilities\\screenshots\\message.png')
            self.logger.debug('*** Something went wrong while trying to message group members ***')

