from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv
import time
import random
import os

load_dotenv()

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

        self.email = os.environ["INSTAGRAM_EMAIL"]
        self.password = os.environ["INSTAGRAM_PASSWORD"]
        self.website = "https://www.instagram.com/accounts/login/"

    def login(self):
        self.driver.get(self.website)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Decline optional cookies')]").click()
        time.sleep(1)
        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(self.email)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(60)
    
    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefboylee/")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x5n08af.x9n4tj2._a6hd').click()
        time.sleep(3)
        follower_popup = self.driver.find_element(By.CSS_SELECTOR, '.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6')
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)
            time.sleep(2)

    def follow(self):
        follower_list = self.driver.find_elements(By.CSS_SELECTOR, ".x1dm5mii")
        for follower in follower_list:
            try:
                follower.find_element(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-._ap30").click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()
            except NoSuchElementException:
                self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()