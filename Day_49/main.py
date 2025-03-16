from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time
import random
import os

load_dotenv()

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4190644401&f_AL=true&f_E=4&f_SB2=44&geoId=102257491&keywords=software%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER")

#Click sign in
driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button').click()

time.sleep(0.5)

#Fill in email/password
email_field = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_field.send_keys(os.environ["LINKEDIN_EMAIL"])
password_field = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_field.send_keys(os.environ["LINKEDIN_PASSWORD"])
password_field.send_keys(Keys.ENTER)
time.sleep(10)

jobs = driver.find_elements(By.CSS_SELECTOR, "main ul .scaffold-layout__list-item")
for job in jobs:
    try:
        job.click()
        time.sleep(1)
        apply_button = driver.find_element(By.CSS_SELECTOR, ".mt4 .jobs-s-apply .jobs-apply-button--top-card button").click()
        time.sleep(2)
        number_input = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--input")
        number_input.clear()
        number_input.send_keys("07906533604")
        submit = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit.text == "Submit application":
            submit.click()
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            time.sleep(1)
        else:
            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button").click()
            time.sleep(1)
    except NoSuchElementException:
        continue

driver.quit()