from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.co.uk/Instant-WhisperQuiet-Multi-Cooker-Smart-Cooker/dp/B0BYSZYRZH")

# time.sleep(5)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# input("")
# driver.quit()

driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li")
events_dict = {i:{"time": n.find_element(By.TAG_NAME, "time").text, "name": n.find_element(By.TAG_NAME, "a").text} for i, n in enumerate(events)}

print(events_dict)