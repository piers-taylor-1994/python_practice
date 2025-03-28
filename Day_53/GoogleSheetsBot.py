import os
from dotenv import load_dotenv
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

load_dotenv()

class GoogleSheetsBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

        self.website = os.environ["GOOGLE_FORM_URL"]

    def fill_in_google_sheets(self, apartments):
        for key,value in apartments.items():
            try:
                self.driver.get(self.website)
                time.sleep(1)
                address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')#
                address.send_keys(value["address"])
                price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price.send_keys(value["price"][:6])
                link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link.send_keys(value["link"])
                self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
                time.sleep(0.5)
            except NoSuchElementException or ElementClickInterceptedException:
                pass
        print(f"{len(apartments)} apartments added!")

