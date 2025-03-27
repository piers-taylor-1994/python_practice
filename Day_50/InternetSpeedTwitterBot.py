from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv()

class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome()
        self.down = down
        self.up = up
        self.twitter_email = os.environ["TWITTER_EMAIL"]
        self.twitter_password = os.environ["TWITTER_PASSWORD"]
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        time.sleep(5)
        self.recorded_download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.recorded_upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.recorded_download}\nup: {self.recorded_upload}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(4)
        email = self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-1mmae3n.r-1e084wi.r-13qz1uu input")
        email.send_keys(self.twitter_email)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-1e084wi.r-13qz1uu input")
        password.send_keys(self.twitter_password)
        password.send_keys(Keys.ENTER)
        time.sleep(5)